import pygame
from pygame.locals import *
import resources.Resources as Resources

class PlayerTurnIndicator:
    def __init__(self):
        
        # Create font and text color
        font = pygame.font.SysFont("arial", 60)
        textColor = (255, 0, 0)

        # Setup text
        self.text = "YOUR TURN"
        self.textWidth, self.textHeight = font.size(self.text)
        self.text = font.render(self.text, 1, textColor)

    def draw(self, screen):
        screen.blit(
            self.text,
            ((screen.get_width() / 2) - (self.textWidth / 2), 0)
        )