import pygame
from pygame.locals import *
from ui.screens.Screen import Screen
from ui.widgets.Button import Button
from game.logic.GameState import GameState
from ui.widgets.TextBox import TextBox
import resources.Resources as Resources
pygame.font.init()

class TitleScreen(Screen):
    def __init__(self):
        
        # Call screen constructor
        Screen.__init__(self)

        # Start button
        self.startButton = Button(200, 50, (Resources.SCREEN_WIDTH / 2) - 100, (Resources.SCREEN_HEIGHT / 2) - 25, (255, 255, 255), (0, 0, 0), "START")

        # Options button
        self.optionsButton = Button(200, 50, (Resources.SCREEN_WIDTH / 2) - 100, (Resources.SCREEN_HEIGHT / 2) + 30, (255, 255, 255), (0, 0, 0), "OPTIONS")

        # Quit button
        self.quitButton = Button(200, 50, (Resources.SCREEN_WIDTH / 2) - 100, (Resources.SCREEN_HEIGHT / 2) + 85, (255, 255, 255), (0, 0, 0), "QUIT")

        # Text botx to enter username
        self.textBox = TextBox((Resources.SCREEN_WIDTH / 2) - 100, (Resources.SCREEN_HEIGHT / 2) - 80, 200, 50)

        self.showError = False

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

                        # Check if start button was clicked
                        if self.startButton.isClicked(event.pos):
                            if len(self.textBox.text) == 0:
                                self.showError = True
                            else:
                                return GameState.NEWGAME, self.textBox.text # TODO: Look into if there's a better way to get this textbox input to the GameScreen other than returning the value here

                        # Check if options button was clicked
                        if self.optionsButton.isClicked(event.pos):
                            return GameState.OPTIONS, None

                        # Check if quit button was clicked
                        if self.quitButton.isClicked(event.pos):
                            return GameState.QUIT

                # Proceed to game if enter is pressed in the textbox
                isInputEntered = self.textBox.handle_event(event)
                if isInputEntered and len(self.textBox.text) != 0:
                    return GameState.NEWGAME, self.textBox.text
                elif isInputEntered and len(self.textBox.text) == 0:
                    self.showError = True

            # Draw everything to the screen
            self.draw()

    def draw(self):
    
        # Blit the background of the screen
        self.screen.blit(self.background, (0, 0))
        
        # Draw buttons and stuff
        self.startButton.draw(self.screen)
        self.optionsButton.draw(self.screen)
        self.quitButton.draw(self.screen)
        self.textBox.draw(self.screen)

        # Show error if username field is left blank
        if self.showError:
            self.displayInputError()

        pygame.display.flip()

    def displayInputError(self):

        # Draw text to screen
        font = pygame.font.SysFont("arial", 15)
        textColor = (255, 0, 0)
        text = "*Username must not be blank"
        text = font.render(text, 1, textColor)
        self.screen.blit(text, ((Resources.SCREEN_WIDTH / 2) - 100, (Resources.SCREEN_HEIGHT / 2) - 100))
