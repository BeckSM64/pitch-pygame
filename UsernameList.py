import pygame
from pygame.locals import *
pygame.font.init()

class UsernameList:
    def __init__(self):

        # Screen width and height
        self.w, self.h = pygame.display.get_surface().get_size()

    def draw(self, game, screen):

        y = 25
        for player in game.players:

            text = str(player.username)
            
            # Draw text to screen
            font = pygame.font.SysFont("arial", 25)
            textColor = (0, 0, 0)

            # If it's the player's turn, highlight their name
            if player.playerTurn:
                textColor = (255, 0, 0)

            text = font.render(text, 1, textColor)
            screen.blit(text, (0, (y * player.id)))
