import pygame
from pygame import display
from pygame.locals import *
from ui.screens.Screen import Screen
from ui.widgets.Button import Button
from game.logic.GameState import GameState
from ui.widgets.TextBox import TextBox
import resources.Resources as Resources

pygame.font.init()


class VideoSettingsScreen(Screen):
    def __init__(self):
        Screen.__init__(self)

        # 504p button
        self.fiveOFourButton = Button(
            200,
            50,
            (Resources.SCREEN_WIDTH / 2) - 100,
            (Resources.SCREEN_HEIGHT / 2) - 135,
            (255, 255, 255),
            (0, 0, 0),
            "896 x 504",
        )

        # 648p button
        self.sixFourtyEightButton = Button(
            200,
            50,
            (Resources.SCREEN_WIDTH / 2) - 100,
            (Resources.SCREEN_HEIGHT / 2) - 80,
            (255, 255, 255),
            (0, 0, 0),
            "1152 x 648",
        )

        # 720p button
        self.sevenTwentyButton = Button(
            200,
            50,
            (Resources.SCREEN_WIDTH / 2) - 100,
            (Resources.SCREEN_HEIGHT / 2) - 25,
            (255, 255, 255),
            (0, 0, 0),
            "1280 x 720",
        )

        # Fullscreen button
        self.fullScreenButton = Button(
            200,
            50,
            (Resources.SCREEN_WIDTH / 2) - 100,
            (Resources.SCREEN_HEIGHT / 2) + 30,
            (255, 255, 255),
            (0, 0, 0),
            "FULLSCREEN",
        )

        # Back button
        self.mainMenuButton = Button(
            200,
            50,
            (Resources.SCREEN_WIDTH / 2) - 100,
            (Resources.SCREEN_HEIGHT / 2) + 85,
            (255, 255, 255),
            (0, 0, 0),
            "MAIN MENU",
        )

        # List of buttons
        self.buttonList.append(self.fiveOFourButton)
        self.buttonList.append(self.sixFourtyEightButton)
        self.buttonList.append(self.sevenTwentyButton)
        self.buttonList.append(self.fullScreenButton)
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

                        # Check if the 504p button was clicked
                        if self.fiveOFourButton.isClicked(event.pos):
                            self.updateUi(896, 504)

                        # Check if the 648p button was clicked
                        if self.sixFourtyEightButton.isClicked(event.pos):
                            self.updateUi(1152, 648)

                        # Check if the 720p button was clicked
                        if self.sevenTwentyButton.isClicked(event.pos):
                            self.updateUi(1280, 720)

                        # Check if the fullscreen button was clicked
                        if self.fullScreenButton.isClicked(event.pos):
                            self.updateUi(1920, 1080, True)

                        # Check if back button was clicked
                        if self.mainMenuButton.isClicked(event.pos):
                            return GameState.TITLE

                # Check if mouse is hovering over button
                self.isMouseHoveringOverButtons()

            # Draw everything to the screen
            self.draw()

    def draw(self):

        # Blit the background of the screen
        self.screen.blit(self.background, (0, 0))

        # Draw buttons and stuff
        self.fiveOFourButton.draw(self.screen)
        self.sixFourtyEightButton.draw(self.screen)
        self.sevenTwentyButton.draw(self.screen)
        self.fullScreenButton.draw(self.screen)
        self.mainMenuButton.draw(self.screen)
        self.displayTitle()

        pygame.display.flip()

    def displayTitle(self):

        # Draw text to screen
        textColor = (0, 0, 0)
        text = "VIDEO SETTINGS"
        textWidth, textHeight = Resources.FONT_TWENTY_FIVE.size(text)
        text = Resources.FONT_TWENTY_FIVE.render(text, 1, textColor)
        self.screen.blit(text, ((Resources.SCREEN_WIDTH / 2) - (textWidth / 2), 0))

    def updateUi(self, width, height, fullscreen=False):

        # Resize the screen
        self.screen, self.background = Resources.set_screen_size(width, height, fullscreen)

        # Update positions of other widgets
        self.fiveOFourButton.setPos(
            (Resources.SCREEN_WIDTH / 2) - 100, (Resources.SCREEN_HEIGHT / 2) - 135
        )
        self.sixFourtyEightButton.setPos(
            (Resources.SCREEN_WIDTH / 2) - 100, (Resources.SCREEN_HEIGHT / 2) - 80
        )
        self.sevenTwentyButton.setPos(
            (Resources.SCREEN_WIDTH / 2) - 100, (Resources.SCREEN_HEIGHT / 2) - 25
        )
        self.fullScreenButton.setPos(
            (Resources.SCREEN_WIDTH / 2) - 100, (Resources.SCREEN_HEIGHT / 2) + 30
        )
        self.mainMenuButton.setPos(
            (Resources.SCREEN_WIDTH / 2) - 100, (Resources.SCREEN_HEIGHT / 2) + 85
        )
