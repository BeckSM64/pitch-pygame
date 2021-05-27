import pygame
from pygame.locals import *
from Button import Button

class BidScreen:
    def __init__(self):

        # Screen width and height
        w, h = pygame.display.get_surface().get_size()

        # Initialize buttons for bid screen
        BUTTON_WIDTH  = 100
        BUTTON_HEIGHT = 100
        BUTTON_PADDING = 5
        COLOR         = (255, 255, 255)
        TEXT_COLOR    = (0, 0, 0)

        self.bidButton2    = Button(BUTTON_WIDTH, BUTTON_HEIGHT, (w / 2) - (BUTTON_WIDTH * 2) - (BUTTON_PADDING * 3),  (h / 2) - (BUTTON_HEIGHT / 2), COLOR, TEXT_COLOR, "2")
        self.bidButton3    = Button(BUTTON_WIDTH, BUTTON_HEIGHT, (w / 2) - (BUTTON_WIDTH) - (BUTTON_PADDING), (h / 2) - (BUTTON_HEIGHT / 2), COLOR, TEXT_COLOR, "3")
        self.bidButton4    = Button(BUTTON_WIDTH, BUTTON_HEIGHT, (w / 2) + (BUTTON_PADDING), (h / 2) - (BUTTON_HEIGHT / 2), COLOR, TEXT_COLOR, "4")
        self.bidButtonPass = Button(BUTTON_WIDTH, BUTTON_HEIGHT, (w / 2) + (BUTTON_WIDTH) + (BUTTON_PADDING * 3), (h / 2) - (BUTTON_HEIGHT / 2), COLOR, TEXT_COLOR, "PASS")

        # List of bid buttons
        self.buttonList = [self.bidButton2, self.bidButton3, self.bidButton4, self.bidButtonPass]

    def draw(self, screen):

        # Draw the buttons to the screen
        self.bidButton2.draw(screen)
        self.bidButton3.draw(screen)
        self.bidButton4.draw(screen)
        self.bidButtonPass.draw(screen)
