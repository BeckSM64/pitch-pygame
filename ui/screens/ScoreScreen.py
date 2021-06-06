import pygame
from pygame.locals import *
pygame.font.init()

class ScoreScreen:
    def __init__(self):

        # Screen width and height
        w, h = pygame.display.get_surface().get_size()

    def draw(self, game, screen):

        x = 200
        for player in game.players:

            text = player.username + ": " + str(player.score)
            
            # Draw text to screen
            font = pygame.font.SysFont("arial", 25)
            textColor = (0, 0, 0)
            text = font.render(text, 1, textColor)
            screen.blit(text, (x * player.id, 0))
