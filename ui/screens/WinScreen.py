import pygame
import resources.Resources as Resources
from pygame.locals import *

class WinScreen:
    def __init__(self):

        # Screen width and height
        self.w, self.h = pygame.display.get_surface().get_size()

    def draw(self, game, screen):
        
        # Display the win message
        self.displayWinMessage(game, screen)

    def displayWinMessage(self, game, screen):

        # Get the list of usernames for who won
        winnerList = game.getWinners()

        # Draw text to screen
        textColor = (0, 0, 0)

        # Create text to display to screen
        text = "Winner(s): "
        for winner in winnerList:
            text += winner

        # Get the size of the text
        textWidth, textHeight = Resources.FONT_TWENTY_FIVE.size(text)
        text = Resources.FONT_TWENTY_FIVE.render(text, 1, textColor)

        # Blit to the screen
        screen.blit(
            text,
            (
                (Resources.SCREEN_WIDTH / 2) - (textWidth / 2),
                (Resources.SCREEN_HEIGHT / 2) - 100,
            ),
        )
