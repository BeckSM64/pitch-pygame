import pygame
from pygame.locals import *
import os
from resources.Resources import *
import resources.Resources as Resources
from ui.screens.Screen import Screen
from game.logic.Game import Game
from game.objects.Card import Card
from game.objects.Hand import Hand
from game.objects.Deck import Deck
from game.objects.MainPile import MainPile
from network.Network import Network
from network.ServerData import *
from game.objects.Trump import Trump
from game.objects.Arrow import Arrow
from ui.widgets.Button import Button
from ui.screens.BidScreen import BidScreen
from ui.screens.ScoreScreen import ScoreScreen
from game.logic.GameState import GameState
from ui.widgets.UsernameList import UsernameList

class GameScreen(Screen):
    def __init__(self, username):
        Screen.__init__(self)

        # Set up connection to server
        self.n = Network()
        self.player = self.n.getP()

        # Handle error connecting to server
        if self.player is None:
            return GameState.SERVER_ERROR
        
        # For debugging
        print("You are player", self.player)

        # Get game
        self.game = self.n.send("get")

        # Set player username
        self.game.players[self.player].username = username
        self.n.send("username: " + username)

        # Initialize test hand
        self.test_hand = get_hand(self.game.players[self.player].playerHand)

        # Initialize main pile to play cards into
        self.main_pile = MainPile()

        # Initialize trump image
        self.trump_image = None

        # Initialize arrow image
        self.arrow_image = Arrow()

        # Initialize bid screen
        self.bid_screen = BidScreen()

        # Initialize username list
        self.username_list = UsernameList()

        # Score button
        SCORE_BUTTON_WIDTH      = 50
        SCORE_BUTTON_HEIGHT     = 50
        SCORE_BUTTON_X          = self.screen.get_width() - SCORE_BUTTON_WIDTH
        SCORE_BUTTON_Y          = 0
        SCORE_BUTTON_COLOR      = (255, 255, 255)
        SCORE_BUTTON_TEXT_COLOR = (0, 0, 0)
        SCORE_BUTTON_TEXT       = "S"

        self.scoreButton = Button(
            SCORE_BUTTON_WIDTH,
            SCORE_BUTTON_HEIGHT,
            SCORE_BUTTON_X,
            SCORE_BUTTON_Y,
            SCORE_BUTTON_COLOR,
            SCORE_BUTTON_TEXT_COLOR,
            SCORE_BUTTON_TEXT
        )

        # Ten and Under Button
        TEN_AND_UNDER_BUTTON_WIDTH      = 100
        TEN_AND_UNDER_BUTTON_HEIGHT     = 100
        TEN_AND_UNDER_BUTTON_PADDING    = 10
        TEN_AND_UNDER_BUTTON_X          = ((self.screen.get_width() / 2) - (TEN_AND_UNDER_BUTTON_WIDTH / 2))
        TEN_AND_UNDER_BUTTON_Y          = ((self.screen.get_height() / 2) - (TEN_AND_UNDER_BUTTON_HEIGHT / 2)) - (TEN_AND_UNDER_BUTTON_HEIGHT + TEN_AND_UNDER_BUTTON_PADDING)
        TEN_AND_UNDER_BUTTON_COLOR      = (255, 0, 0)
        TEN_AND_UNDER_BUTTON_TEXT_COLOR = (0, 0, 0)
        TEN_AND_UNDER_BUTTON_TEXT       = "TEN\nAND\nUNDER"

        self.tenAndUnderButton = Button(
            TEN_AND_UNDER_BUTTON_WIDTH,
            TEN_AND_UNDER_BUTTON_HEIGHT,
            TEN_AND_UNDER_BUTTON_X,
            TEN_AND_UNDER_BUTTON_Y,
            TEN_AND_UNDER_BUTTON_COLOR,
            TEN_AND_UNDER_BUTTON_TEXT_COLOR,
            TEN_AND_UNDER_BUTTON_TEXT
        )

        # Score screen
        self.scoreScreen = ScoreScreen()

        self.showGameScreen = False
        self.showScoreScreen = False
        self.gameReady = False

    def run(self):

        # Game loop
        while True:
            self.clock.tick(60)

            # Attempt to get the game from the server
            try:
                    
                self.game = self.n.send("get")
                
                # If a player left the game (numPlayers decreased),
                # disconnect from server and return to the title screen
                if self.game.numPlayers != len(self.game.players):
                    self.n.disconnect()
                    return GameState.DISCONNECT

                # Check to see if game is ready to start
                if self.game.numPlayers >= 3 and self.showScoreScreen == False:
                    self.gameReady = True
                    self.showGameScreen = True

                # Update main pile
                self.main_pile = get_main_pile(self.game.mainPile)

                # Set trump image
                if self.game.trump is not None and self.trump_image != self.game.trump:
                    self.trump_image = Trump(self.game.trump)
                else:
                    self.trump_image = None

                # Update hand
                if self.game.players[self.player].ready:
                    self.test_hand = get_hand(self.game.players[self.player].playerHand)
                    self.n.send("not ready")

            except:
                print("Couldn't get game")

            for event in pygame.event.get():

                # Check for quit event
                if event.type == QUIT:
                    return GameState.QUIT

                # Check for click event
                if event.type == pygame.MOUSEBUTTONUP and self.gameReady:
                    if event.button == 1: # the right mouse button
                        for card in self.test_hand:

                            # Only play card if it is this player's turn
                            if (
                                    card.rect.collidepoint(event.pos) and self.game.players[self.player].playerTurn and
                                    self.game.players[self.player].playerBid is not None and self.game.didPlayersBid() == True and
                                    card.isPlayable(self.game, self.test_hand.hasCurrentSuit(self.game.currentSuit))
                                ):
                                self.test_hand.remove(card)

                                # Set not ready
                                if len(self.test_hand) == 0:
                                    self.n.send("not ready")

                                # Send card to server
                                self.n.send("card: " + str(card.value) + " " + card.suit)
                            
                        # Check if a bid button was clicked
                        if self.game.players[self.player].playerBidTurn and self.game.biddingStage:
                            for button in self.bid_screen.buttonList:
                                if button.isClicked(event.pos):
                                    self.n.send("bid: " + button.text)

                        # Check if score button was clicked
                        if self.scoreButton.isClicked(event.pos) and self.showGameScreen == True:
                            self.showGameScreen = False
                            self.showScoreScreen = True
                        elif self.scoreButton.isClicked(event.pos) and self.showScoreScreen == True:
                            self.showGameScreen = True
                            self.showScoreScreen = False

                        # Check if ten and under button was clicked
                        if self.hasTenAndUnder():
                            if self.tenAndUnderButton.isClicked(event.pos) and self.showGameScreen == True:

                                # Alert the server that player is turning in ten and under
                                self.n.send("tenAndUnder")

                                # Update the game for the client
                                self.game = self.n.send("get")

                                # Get the new player hand from the updated game
                                self.test_hand = get_hand(self.game.players[self.player].playerHand)
            self.draw()

    def draw(self):

        if self.showGameScreen == True:

            # Blit the background of the screen
            self.screen.blit(self.background, (0, 0))

            # Draw the hand on the screen
            self.test_hand.draw(self.screen)

            # Draw the main pile to the screen
            self.main_pile.draw(self.screen)

            # Draw the trump image to the screen
            if self.trump_image is not None:
                self.trump_image.draw(self.screen)

            # Draw arrow image when it is player's turn
            if self.game.players[self.player].playerTurn:
                self.arrow_image.draw(self.screen)

            # Draw the bid screen
            if self.game.biddingStage and self.game.players[self.player].playerBidTurn:
                self.bid_screen.draw(self.screen, self.game)

            # Draw score button
            self.scoreButton.draw(self.screen)

            # Draw the ten and under button
            if self.hasTenAndUnder():
                self.tenAndUnderButton.draw(self.screen)

            # Draw the username list
            self.username_list.draw(self.game, self.screen)

            pygame.display.flip()

            # Time delay to keep the last card on screen in trick
            if self.game.mainPile.size() % len(self.game.players) == 0 and self.game.mainPile.size() != 0 and not self.game.isPlayersReady():
                pygame.time.delay(2000)
                self.n.send("ready")

        if self.showScoreScreen == True:

            # Blit everything to the screen
            self.screen.blit(self.background, (0, 0))

            # Draw score button
            self.scoreButton.draw(self.screen)

            self.scoreScreen.draw(self.game, self.screen)

            pygame.display.flip()

        if self.gameReady == False:

            # Blit everything to the screen
            self.screen.blit(self.background, (0, 0))

            self.displayWaitMessage()

            pygame.display.flip()

    def hasTenAndUnder(self):
        """Player has a ten and under that meets the criteria to turn in"""

        return (

            # Players are actively bidding
            self.game.isBiddingStage() and

            # Player's turn to bid
            self.game.players[self.player].playerBidTurn and

            # Player has a ten and under
            self.test_hand.hasTenAndUnder() and

            (
                # Player is not the last bidder
                (self.game.getNumberOfBids() < (self.game.numPlayers - 1)) or

                # Player is the last bidder and someone has bid already
                ((self.game.getNumberOfBids() == (self.game.numPlayers - 1)) and (self.game.getHighestBid() > 0))
            )
        )


    def displayWaitMessage(self):

        # Draw text to screen
        font = pygame.font.SysFont("arial", 30)
        textColor = (0, 0, 0)
        text = "Waiting For More Players..."
        textWidth, textHeight = font.size(text)
        text = font.render(text, 1, textColor)
        self.screen.blit(text, ((Resources.SCREEN_WIDTH / 2) - (textWidth / 2), (Resources.SCREEN_HEIGHT / 2) - (textHeight / 2)))
