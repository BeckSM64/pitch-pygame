import pygame
import resources.Resources as Resources
from pygame.locals import *

pygame.font.init()


class Button:
    def __init__(self, width, height, x, y, color, textColor, text):

        # Constants
        self.UNFILLED_BUTTON_BORDER_WIDTH = 3
        self.FILLED_BUTTON_BORDER_WIDTH = 0
        self.TEXT_COLOR = textColor

        # Members
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.textColor = textColor
        self.rect = Rect(x, y, width, height)
        self.borderWidth = self.UNFILLED_BUTTON_BORDER_WIDTH

        # For multiline text, split on new line character
        self.textList = text.split("\n")

    def draw(self, screen):

        # Draw rectangle to screen
        pygame.draw.rect(
            screen, (0, 0, 0), self.rect, border_radius=5, width=self.borderWidth
        )

        # Render font render on text in text list
        textRenderList = []
        for textElement in self.textList:
            textRenderList.append(
                Resources.FONT_FIFTEEN.render(textElement, 1, self.textColor)
            )

        # Loop through list of indivual lines of text and blit to screen
        for i in range(len(textRenderList)):

            # Get the text width and height
            textWidth, textHeight = Resources.FONT_FIFTEEN.size(self.textList[i])

            # Blit the text to the screen (over the button)
            screen.blit(
                textRenderList[i],
                (
                    self.x + ((self.width / 2) - textRenderList[i].get_width() / 2),
                    self.y
                    + (
                        ((self.height / (len(textRenderList) + 1)) * (i + 1))
                        - (textHeight / 2)
                    ),
                ),
            )

    def isClicked(self, eventPos):
        if self.rect.collidepoint(eventPos):
            return True
        else:
            return False

    def isHovering(self, mousePos):
        if self.rect.collidepoint(mousePos):
            self.borderWidth = self.FILLED_BUTTON_BORDER_WIDTH
            self.textColor = Resources.BACKGROUND_COLOR
        else:
            self.borderWidth = self.UNFILLED_BUTTON_BORDER_WIDTH
            self.textColor = self.TEXT_COLOR

    def setPos(self, x, y):

        # Update x and y position
        self.x = x
        self.y = y

        # Recreate rectangle
        self.rect = Rect(self.x, self.y, self.width, self.height)
