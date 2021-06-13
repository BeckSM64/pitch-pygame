import pygame
from pygame.locals import *
pygame.font.init()

class Button:
    def __init__(self, width, height, x, y, color, textColor, text):

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.textColor = textColor
        self.rect = Rect(x, y, width, height)
        
        # For multiline text, split on new line character
        self.textList = text.split("\n")

    def draw(self, screen):

        # Draw rectangle to screen
        pygame.draw.rect(screen, self.color, self.rect, border_radius = 5)

        # Draw text to screen
        font = pygame.font.SysFont("arial", 15)

        # Render font render on text in text list
        textRenderList = []
        for textElement in self.textList:
            textRenderList.append(font.render(textElement, 1, self.textColor))

        # Loop through list of indivual lines of text and blit to screen
        for i in range(len(textRenderList)):

            # Get the text width and height
            textWidth, textHeight = font.size(self.textList[i])

            # Blit the text to the screen (over the button)
            screen.blit(
                textRenderList[i],
                (
                    self.x + ((self.width / 2) - textRenderList[i].get_width()/2),
                    self.y + (((self.height / (len(textRenderList) + 1)) * (i + 1)) - (textHeight / 2))
                )
            )

    def isClicked(self, eventPos):
        if self.rect.collidepoint(eventPos):
            return True
        else:
            return False

    def setPos(self, x, y):

        # Update x and y position
        self.x = x
        self.y = y

        # Recreate rectangle
        self.rect = Rect(self.x, self.y, self.width, self.height)
