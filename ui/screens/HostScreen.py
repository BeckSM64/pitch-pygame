import pygame
from pygame.locals import *
from ui.screens.Screen import Screen
from ui.widgets.Button import Button
from game.logic.GameState import GameState
from ui.widgets.TextBox import TextBox
from ui.widgets.Incrementer import Incrementer
import resources.Resources as Resources
pygame.font.init()

class HostScreen(Screen):
    def __init__(self):

        # Call Screen constructor
        Screen.__init__(self)

        # Host button
        self.hostButton = Button(
            200,
            50,
            (Resources.SCREEN_WIDTH / 2) - 100,
            (Resources.SCREEN_HEIGHT / 2) - 25,
            (255, 255, 255), (0, 0, 0),
            "HOST GAME"
        )

        # Back button
        self.mainMenuButton = Button(
            200,
            50, (Resources.SCREEN_WIDTH / 2) - 100,
            (Resources.SCREEN_HEIGHT / 2) + 30,
            (255, 255, 255), (0, 0, 0),
            "MAIN MENU"
        )

        # List of buttons
        self.buttonList.append(self.hostButton)
        self.buttonList.append(self.mainMenuButton)

        # Text box to enter game name
        self.textBox = TextBox(
            (Resources.SCREEN_WIDTH / 2) - 100,
            (Resources.SCREEN_HEIGHT / 2) - 80,
            200,
            50
        )

        # Game mode incrementer
        gameModeOptions = ["Normal", "Jick"]
        self.gameModeIncrementer = Incrementer(gameModeOptions)
        INCREMENTER_X = (Resources.SCREEN_WIDTH / 2) - (self.gameModeIncrementer.incrementerWidth / 2)
        INCREMENTER_Y = 40
        self.gameModeIncrementer.setPos(INCREMENTER_X, INCREMENTER_Y)

        # Number of players incrementer
        numPlayersOptions = ["3", "4"]
        self.numPlayersIncrementer = Incrementer(numPlayersOptions)
        INCREMENTER_X = (Resources.SCREEN_WIDTH / 2) - (self.numPlayersIncrementer.incrementerWidth / 2)
        INCREMENTER_Y = 90
        self.numPlayersIncrementer.setPos(INCREMENTER_X, INCREMENTER_Y)

        # Flag to show textbox input error
        self.showError = False

    def run(self):

        # Game loop
        while True:
            self.clock.tick(60)

            for event in pygame.event.get():

                # Check for quit event
                if event.type == QUIT:
                    return GameState.QUIT, None, None, None, None, None

                # Check for click event
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1: # the right mouse button

                        # Check if host button was clicked
                        if self.hostButton.isClicked(event.pos):
                            if len(self.textBox.text) == 0:
                                self.showError = True
                            else:
                                return GameState.NEWGAME, True, self.textBox.text, None, int(self.numPlayersIncrementer.activeOption), self.gameModeIncrementer.activeOption

                        # Check if back button was clicked
                        if self.mainMenuButton.isClicked(event.pos):
                            return GameState.TITLE, False, None, None, None, None

                        # Handle input for incrementers
                        self.gameModeIncrementer.handleInput(event.pos)
                        self.numPlayersIncrementer.handleInput(event.pos)

                # Proceed to game if enter is pressed in the textbox
                isInputEntered = self.textBox.handle_event(event)
                if isInputEntered and len(self.textBox.text) != 0:
                    return GameState.NEWGAME, True, self.textBox.text, None, int(self.numPlayersIncrementer.activeOption), self.gameModeIncrementer.activeOption
                elif isInputEntered and len(self.textBox.text) == 0:
                    self.showError = True

                # Check if mouse is hovering over buttons
                self.isMouseHoveringOverButtons()

            # Draw everything to the screen
            self.draw()

    def draw(self):
    
        # Blit the background of the screen
        self.screen.blit(self.background, (0, 0))
        
        # Draw buttons and stuff
        self.hostButton.draw(self.screen)
        self.mainMenuButton.draw(self.screen)
        self.textBox.draw(self.screen)
        self.gameModeIncrementer.draw(self.screen)
        self.numPlayersIncrementer.draw(self.screen)
        self.displayTitle()

        if self.showError:
            self.displayInputError()

        pygame.display.flip()

    def displayTitle(self):

        # Draw text to screen
        font = pygame.font.SysFont("arial", 25)
        textColor = (0, 0, 0)
        text = "HOST"
        textWidth, textHeight = font.size(text)
        text = font.render(text, 1, textColor)

        self.screen.blit(
            text,
            ((Resources.SCREEN_WIDTH / 2) - (textWidth / 2),
            0)
        )

    def displayInputError(self):

        # Draw text to screen
        font = pygame.font.SysFont("arial", 15)
        textColor = (255, 0, 0)
        text = "*Game name must not be blank"
        text = font.render(text, 1, textColor)
        
        self.screen.blit(
            text, 
            ((Resources.SCREEN_WIDTH / 2) - 100,
            self.textBox.y - 20)
        )
