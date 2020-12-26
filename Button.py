import pygame
from pygame.locals import *
pygame.font.init()

class Button:
    def __init__(self, width, height, x, y, color, text):

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.rect = Rect(x, y, width, height)

    def draw(self, screen):

        # Draw rectangle to screen
        pygame.draw.rect(screen, (0, 0, 0), self.rect)

        # Draw text to screen
        font = pygame.font.SysFont("arial", 15)
        text = font.render(self.text, 1, self.color, True)
        screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
