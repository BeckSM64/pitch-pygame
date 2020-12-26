import pygame
from pygame.locals import *
from Button import Button

class BidScreen:
    def __init__(self):

        # Screen width and height
        w, h = pygame.display.get_surface().get_size()

        # Initialize buttons for bid screen
        buttonWidth = 100
        buttonHeight = 100
        color = (255, 255, 255)
        self.bidButton2    = Button(buttonWidth, buttonHeight, 10,  (h / 2) - (buttonHeight / 2), color, "2")
        self.bidButton3    = Button(buttonWidth, buttonHeight, 120, (h / 2) - (buttonHeight / 2), color, "3")
        self.bidButton4    = Button(buttonWidth, buttonHeight, 230, (h / 2) - (buttonHeight / 2), color, "4")
        self.bidButtonPass = Button(buttonWidth, buttonHeight, 340, (h / 2) - (buttonHeight / 2), color, "PASS")

        # List of bid buttons
        self.buttonList = [self.bidButton2, self.bidButton3, self.bidButton4, self.bidButtonPass]

    def draw(self, screen):

        # Draw the buttons to the screen
        self.bidButton2.draw(screen)
        self.bidButton3.draw(screen)
        self.bidButton4.draw(screen)
        self.bidButtonPass.draw(screen)
