import pygame
from pygame.locals import *
import os
from Resources import *
from Game import Game
from Card import Card
from Hand import Hand
from Deck import Deck
from MainPile import MainPile
from Network import Network
from ServerData import *
from Trump import Trump
from Arrow import Arrow
from Button import Button
from BidScreen import BidScreen
from ScoreScreen import ScoreScreen
from GameState import GameState

def gameScreen(gameKey):

    print("GAME KEY", gameKey)

    # Clock
    clock = pygame.time.Clock()

    # Set up connection to server
    n = Network()
    n.connect()

    # Get game
    game = n.send("gameKey " + gameKey)

    player = int(n.getP("player"))
    print("You are player", player)

    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode((450, 500))
    pygame.display.set_caption('Pitch')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 250, 250))

    # Initialize test hand
    test_hand = get_hand(game.players[player].playerHand)

    # Initialize main pile to play cards into
    main_pile = MainPile()

    # Initialize trump image
    trump_image = None

    # Initialize arrow image
    arrow_image = Arrow()

    # Initialize bid screen
    bid_screen = BidScreen()

    # Score button
    scoreButton = Button(50, 50 , 400, 0, (255, 255, 255), (0, 0, 0), "S")

    # Score screen
    scoreScreen = ScoreScreen()

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    run = True
    showGameScreen = True
    showScoreScreen = False

    # Game loop
    while run:
        clock.tick(60)

        # Attempt to get the game from the server
        try:
                
            game = n.send("get")

            # Update main pile
            main_pile = get_main_pile(game.mainPile)

            # Set trump image
            if game.trump is not None and trump_image != game.trump:
                trump_image = Trump(game.trump)
            else:
                trump_image = None

            # Update hand
            if game.players[player].ready:
                test_hand = get_hand(game.players[player].playerHand)
                n.send("not ready")

        except:
            print("Couldn't get game")

        for event in pygame.event.get():

            # Check for quit event
            if event.type == QUIT:
                return GameState.QUIT

            # Check for click event
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: # the right mouse button
                    for card in test_hand:

                        # Only play card if it is this player's turn
                        if (
                                card.rect.collidepoint(event.pos) and game.players[player].playerTurn and
                                game.players[player].playerBid is not None and game.didPlayersBid() == True and
                                card.isPlayable(game, test_hand.hasCurrentSuit(game.currentSuit))
                            ):
                            test_hand.remove(card)

                            # Set not ready
                            if len(test_hand) == 0:
                                n.send("not ready")

                            # Send card to server
                            n.send("card: " + str(card.value) + " " + card.suit)
                        
                    # Check if a bid button was clicked
                    if game.players[player].playerBidTurn and game.biddingStage:
                        for button in bid_screen.buttonList:
                            if button.isClicked(event.pos):
                                n.send("bid: " + button.text)

                    # Check if score button was clicked
                    if scoreButton.isClicked(event.pos) and showGameScreen == True:
                        showGameScreen = False
                        showScoreScreen = True
                    elif scoreButton.isClicked(event.pos) and showScoreScreen == True:
                        showGameScreen = True
                        showScoreScreen = False

        if showGameScreen == True:

            # Blit the background of the screen
            screen.blit(background, (0, 0))

            # Draw the hand on the screen
            test_hand.draw(screen)

            # Draw the main pile to the screen
            main_pile.draw(screen)

            # Draw the trump image to the screen
            if trump_image is not None:
                trump_image.draw(screen)

            # Draw arrow image when it is player's turn
            if game.players[player].playerTurn:
                arrow_image.draw(screen)

            # Draw the bid screen
            if game.biddingStage and game.players[player].playerBidTurn:
                bid_screen.draw(screen)

            # Draw score button
            scoreButton.draw(screen)

            pygame.display.flip()

            # Time delay to keep the last card on screen in trick
            if game.mainPile.size() % len(game.players) == 0 and game.mainPile.size() != 0 and not game.isPlayersReady():
                pygame.time.delay(2000)
                n.send("ready")

        if showScoreScreen == True:

            # Blit everything to the screen
            screen.blit(background, (0, 0))

            # Draw score button
            scoreButton.draw(screen)

            scoreScreen.draw(game, screen)

            pygame.display.flip()
