import pygame
from pygame.locals import *
pygame.font.init()

class ScoreScreen:
    def __init__(self):

        # Screen width and height
        w, h = pygame.display.get_surface().get_size()

    def draw(self, game, screen):

        x = 100
        for player in game.players:

            text = "P" + str(player.id) + ": " + str(player.score)
            
            # Draw text to screen
            font = pygame.font.SysFont("arial", 15)
            text = font.render(text, 1, (0, 0, 0))
            screen.blit(text, (x * player.id, 0))
