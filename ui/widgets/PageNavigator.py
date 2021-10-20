import pygame
from pygame.locals import *
from ui.widgets.Arrow import Arrow
import resources.Resources as Resources


class PageNavigator:
    def __init__(self):

        # Constants for arrows
        LEFT_ARROW_WIDTH = (Resources.SCREEN_WIDTH / 2) - Arrow.width
        LEFT_ARROW_HEIGHT = Resources.SCREEN_HEIGHT - Arrow.height
        LEFT_ARROW_ROTATION = 270
        RIGHT_ARROW_WIDTH = Resources.SCREEN_WIDTH / 2
        RIGHT_ARROW_HEIGHT = Resources.SCREEN_HEIGHT - Arrow.height
        RIGHT_ARROW_ROTATION = 90

        # Create the left and right arrow for navigation
        self.leftArrow = Arrow(LEFT_ARROW_WIDTH, LEFT_ARROW_HEIGHT, LEFT_ARROW_ROTATION)
        self.rightArrow = Arrow(
            RIGHT_ARROW_WIDTH, RIGHT_ARROW_HEIGHT, RIGHT_ARROW_ROTATION
        )

    def isLeftClicked(self, eventPos):
        return self.leftArrow.isClicked(eventPos)

    def isRightClicked(self, eventPos):
        return self.rightArrow.isClicked(eventPos)

    def draw(self, screen):

        # Draw the left and right arrows to the screen
        self.leftArrow.draw(screen)
        self.rightArrow.draw(screen)
