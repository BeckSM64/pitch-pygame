import pygame
from pygame.locals import *
from ui.widgets.Arrow import Arrow
import resources.Resources as Resources
pygame.font.init()

class Incrementer:
    def __init__(self, options):

        # Options
        self.options = options
        
        # Number of options for incrementer
        self.numOptions = len(options)

        # Draw text to screen
        textColor = (0, 0, 0)

        # Create list of text to render
        self.textWidthMap  = {}
        self.maxTextWidth  = -1
        self.maxTextHeight = -1

        # Loop through options and create text to render
        i = 0
        for option in options:
            textWidth, textHeight = Resources.FONT_TWENTY_FIVE.size(option)
            text = Resources.FONT_TWENTY_FIVE.render(option, 1, textColor)

            # Append to text width map
            self.textWidthMap[i] = {text : textWidth}

            # Check if max text width
            if textWidth > self.maxTextWidth:
                self.maxTextWidth = textWidth
            
            # Check if max text height
            if textHeight > self.maxTextHeight:
                self.maxTextHeight = textHeight

            # Increment counter
            i += 1

        self.TEXT_X_POSITION = None
        self.TEXT_Y_POSITION = (((Arrow.height / 2)) - (textHeight / 2))

        # Constants for arrows
        self.LEFT_ARROW_X         = 0
        self.LEFT_ARROW_Y         = 0
        TEXT_X                    = 0 + Arrow.width
        self.RIGHT_ARROW_X        = TEXT_X + self.maxTextWidth
        self.RIGHT_ARROW_Y        = 0
        self.LEFT_ARROW_ROTATION  = 270
        self.RIGHT_ARROW_ROTATION = 90

        # Set the width of the incrementer
        self.incrementerWidth = ((self.RIGHT_ARROW_X + Arrow.width) - self.LEFT_ARROW_X)

        # Create the left and right arrow for navigation
        self.leftArrow  = Arrow(self.LEFT_ARROW_X, self.LEFT_ARROW_Y, self.LEFT_ARROW_ROTATION)
        self.rightArrow = Arrow(self.RIGHT_ARROW_X, self.RIGHT_ARROW_Y, self.RIGHT_ARROW_ROTATION)

        # The active index for the text map
        self.activeTextIndex = 0

        # Option that is currently selected
        self.activeOption = options[0]

    def handleInput(self, eventPos):
        if self.leftArrow.isClicked(eventPos):
            if (self.activeTextIndex - 1) >= 0:
                self.activeTextIndex -= 1

        if self.rightArrow.isClicked(eventPos):
            if (self.activeTextIndex + 1) < self.numOptions:
                self.activeTextIndex += 1

        # Set the active option
        self.activeOption = self.options[self.activeTextIndex]
    
    def setPos(self, x, y):

        # Constants for arrows
        self.LEFT_ARROW_X         = x
        self.LEFT_ARROW_Y         = y
        TEXT_X                    = x + Arrow.width
        self.RIGHT_ARROW_X        = TEXT_X + self.maxTextWidth
        self.RIGHT_ARROW_Y        = y
        self.LEFT_ARROW_ROTATION  = 270
        self.RIGHT_ARROW_ROTATION = 90

        # Recreate the arrows
        self.leftArrow  = Arrow(self.LEFT_ARROW_X, self.LEFT_ARROW_Y, self.LEFT_ARROW_ROTATION)
        self.rightArrow = Arrow(self.RIGHT_ARROW_X, self.RIGHT_ARROW_Y, self.RIGHT_ARROW_ROTATION)

    def draw(self, screen):

        # Draw text to screen
        activeTextMap = self.textWidthMap[self.activeTextIndex]
        for option, width in activeTextMap.items():
            self.TEXT_X_POSITION = ((self.LEFT_ARROW_X + self.incrementerWidth) - (self.incrementerWidth / 2) - (width / 2))
            self.TEXT_Y_POSITION = (((Arrow.height / 2)) - (self.maxTextHeight / 2)) + self.LEFT_ARROW_Y
            screen.blit(option, (self.TEXT_X_POSITION, self.TEXT_Y_POSITION))

        # Draw the left and right arrows to the screen
        self.leftArrow.draw(screen)
        self.rightArrow.draw(screen)
