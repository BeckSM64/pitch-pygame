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

    def draw(self, screen):

        # Draw rectangle to screen
        pygame.draw.rect(screen, self.color, self.rect, border_radius = 5)

        # Draw text to screen
        font = pygame.font.SysFont("arial", 15)
        text = font.render(self.text, 1, self.textColor)
        screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isClicked(self, eventPos):
        if self.rect.collidepoint(eventPos):
            return True
        else:
            return False
