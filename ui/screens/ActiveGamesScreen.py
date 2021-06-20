import pygame
from pygame.locals import *
from ui.screens.Screen import Screen
from ui.widgets.Button import Button
from ui.widgets.ActiveGameButton import ActiveGameButton
from game.logic.GameState import GameState
from ui.widgets.TextBox import TextBox
from network.Network import Network
from game.logic.GameList import GameList
import resources.Resources as Resources
pygame.font.init()

class ActiveGamesScreen(Screen):
    def __init__(self):

        # Call Screen constructor
        Screen.__init__(self)

        # Make connection to the server
        self.n = Network()
        self.n.connect()

        gameList = self.n.send("gameList")
        self.n.disconnect()

        print(gameList.games)

        self.buttonList = []

        # Game buttons
        for game in gameList.games:
            button = ActiveGameButton(
                game,
                200,
                50,
                (Resources.SCREEN_WIDTH / 2) - 100,
                (Resources.SCREEN_HEIGHT / 2) - 25,
                (255, 255, 255), (0, 0, 0),
            )
            self.buttonList.append(button)

    def run(self):

        # Game loop
        while True:
            self.clock.tick(60)

            for event in pygame.event.get():

                # Check for quit event
                if event.type == QUIT:
                    return GameState.QUIT

                # Check for click event
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1: # the right mouse button

                        # Check if game button was clicked
                        for button in self.buttonList:
                            if button.isClicked(event.pos):
                                return GameState.NEWGAME, False, button.gameName

            # Draw everything to the screen
            self.draw()

    def draw(self):
    
        # Blit the background of the screen
        self.screen.blit(self.background, (0, 0))
        
        # Draw buttons and stuff
        for button in self.buttonList:
            button.draw(self.screen)

        pygame.display.flip()
