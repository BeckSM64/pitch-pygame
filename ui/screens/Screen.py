import pygame
from pygame.locals import *
import resources.Resources as Resources

class Screen:
    def __init__(self):
        
        # Clock
        self.clock = pygame.time.Clock()

        # Initialize screen
        pygame.init()
        self.screen = pygame.display.set_mode((Resources.SCREEN_WIDTH, Resources.SCREEN_HEIGHT))
        pygame.display.set_caption('Pitch')

        # Fill background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 250, 250))

        # Blit everything to the screen
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()