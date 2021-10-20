import pygame
from pygame.locals import *
from ui.screens.Screen import Screen
from ui.widgets.Button import Button
from game.logic.GameState import GameState
from ui.widgets.TextBox import TextBox
import resources.Resources as Resources

pygame.font.init()


class DisconnectScreen(Screen):
    def __init__(self):

        # Call screen constructor
        Screen.__init__(self)

        # Back button
        self.mainMenuButton = Button(
            200,
            50,
            (Resources.SCREEN_WIDTH / 2) - 100,
            (Resources.SCREEN_HEIGHT / 2) - 25,
            (255, 255, 255),
            (0, 0, 0),
            "MAIN MENU",
        )

        # Add buttons to button list
        self.buttonList.append(self.mainMenuButton)

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
                    if event.button == 1:  # the right mouse button

                        # Check if back button was clicked
                        if self.mainMenuButton.isClicked(event.pos):
                            return GameState.TITLE

                # Check if mouse is hover over buttons
                self.isMouseHoveringOverButtons()

            self.draw()

    def draw(self):

        # Blit the background of the screen
        self.screen.blit(self.background, (0, 0))

        # Draw buttons and stuff
        self.mainMenuButton.draw(self.screen)
        self.displayError()

        pygame.display.flip()

    def displayError(self):

        # Draw text to screen
        textColor = (255, 0, 0)
        text = "Game ended unexpectedy due to player disconnect"
        textWidth, textHeight = Resources.FONT_TWENTY_FIVE.size(text)
        text = Resources.FONT_TWENTY_FIVE.render(text, 1, textColor)
        self.screen.blit(
            text,
            (
                (Resources.SCREEN_WIDTH / 2) - (textWidth / 2),
                (Resources.SCREEN_HEIGHT / 2) - 100,
            ),
        )
