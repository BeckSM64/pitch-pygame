import pygame
from pygame.locals import *
import resources.Resources as Resources

class Screen:
    def __init__(self):
        
        # Clock
        self.clock = pygame.time.Clock()

        # Set the icon
        self.icon = pygame.image.load(Resources.resolve_path('./resources/diamond.png'))
        pygame.display.set_icon(self.icon)

        # Initialize screen
        pygame.init()
        self.screen = pygame.display.set_mode((Resources.SCREEN_WIDTH, Resources.SCREEN_HEIGHT))
        pygame.display.set_caption('Pitch')

        # Fill background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(Resources.BACKGROUND_COLOR)

        # Blit everything to the screen
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

        # List of buttons
        self.buttonList = []

    def isMouseHoveringOverButtons(self):
        for button in self.buttonList:
            button.isHovering(pygame.mouse.get_pos())
