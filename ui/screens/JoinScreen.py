from ui.widgets.PageNavigator import PageNavigator
from ui.widgets.Arrow import Arrow
import pygame
from pygame.locals import *
from ui.screens.Screen import Screen
from ui.widgets.Button import Button
from ui.widgets.ActiveGameButton import ActiveGameButton
from game.logic.GameState import GameState
from ui.widgets.TextBox import TextBox
from network.Network import Network
from game.logic.GameList import GameList
from ui.widgets.PageNavigator import PageNavigator
import resources.Resources as Resources
pygame.font.init()

class JoinScreen(Screen):
    def __init__(self):

        # Call Screen constructor
        Screen.__init__(self)

        # Make connection to the server
        self.n = Network()
        self.n.connect()

        # Retrieve list of games from server
        self.buttonListSubset = []
        self.buttonList = []
        self.buttonListSlice = [0, 4]
        self.updateGameList()

        # Page navigator to go to next or previous page of active games
        self.pageNavigator = PageNavigator()

    def updateGameList(self):

        gameList = self.n.send("gameList")

        self.buttonList = []

        # Game buttons
        i = 0
        BUTTON_WIDTH   = 400
        BUTTON_HEIGHT  = 100
        BUTTON_PADDING = 5

        # Loop through active games in the game list
        for game in gameList.games:

            # Only create a button for games that have open spots
            if game.maxPlayers != game.numPlayers:
                button = ActiveGameButton(
                    game,
                    BUTTON_WIDTH,
                    BUTTON_HEIGHT,
                    (Resources.SCREEN_WIDTH / 2) - (BUTTON_WIDTH / 2),
                    (0 + BUTTON_HEIGHT + BUTTON_PADDING) * i,
                    (255, 255, 255),
                    (0, 0, 0)
                )
                self.buttonList.append(button)
                i += 1

        # Only display 4 games per page
        if len(self.buttonList) > 4:
            self.buttonListSubset = self.buttonList[self.buttonListSlice[0]:self.buttonListSlice[1]]
        else:
            self.buttonListSubset = self.buttonList

        # Update the positions of all the buttons
        self.updateButtonPositions()

        # Check if mouse is hovering over buttons
        for button in self.buttonListSubset:
            button.isHovering(pygame.mouse.get_pos())

    def updateButtonPositions(self):

        i = 0
        BUTTON_WIDTH   = 400
        BUTTON_HEIGHT  = 100
        BUTTON_PADDING = 5
        for button in self.buttonListSubset:
            button.setPos(
                (Resources.SCREEN_WIDTH / 2) - (BUTTON_WIDTH / 2),
                (0 + BUTTON_HEIGHT + BUTTON_PADDING) * i
            )
            i += 1

    def run(self):

        # Game loop
        while True:
            self.clock.tick(60)

            for event in pygame.event.get():

                # Check for quit event
                if event.type == QUIT:
                    return GameState.QUIT, None, None, None

                # Check for click event
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1: # the right mouse button

                        # Check if game button was clicked
                        for button in self.buttonListSubset:
                            if button.isClicked(event.pos):
                                self.n.disconnect()
                                return GameState.NEWGAME, False, button.gameName, button.gameId

                    if self.pageNavigator.isLeftClicked(event.pos):
                        if 0 <= self.buttonListSlice[0] - 1 < len(self.buttonList):
                            self.buttonListSlice[0] = self.buttonListSlice[0] - 1
                            self.buttonListSlice[1] = self.buttonListSlice[1] - 1

                    if self.pageNavigator.isRightClicked(event.pos):
                        if 0 <= self.buttonListSlice[1] < len(self.buttonList):
                            self.buttonListSlice[1] = self.buttonListSlice[1] + 1
                            self.buttonListSlice[0] = self.buttonListSlice[0] + 1

            # Update game list
            self.updateGameList()

            # Draw everything to the screen
            self.draw()

    def draw(self):
    
        # Blit the background of the screen
        self.screen.blit(self.background, (0, 0))
        
        for button in self.buttonListSubset:
            button.draw(self.screen)
            
        # if there are no active games display error message
        if len(self.buttonList) == 0:
            self.displayError()

        # Draw the page navigator
        self.pageNavigator.draw(self.screen)

        pygame.display.flip()

    def displayError(self):

        # Draw text to screen
        font = pygame.font.SysFont("arial", 25)
        textColor = (0, 0, 0)
        text = "No Active Games"
        textWidth, textHeight = font.size(text)
        text = font.render(text, 1, textColor)
        self.screen.blit(text, ((Resources.SCREEN_WIDTH / 2) - (textWidth / 2), (Resources.SCREEN_HEIGHT / 2) - (textHeight / 2)))
