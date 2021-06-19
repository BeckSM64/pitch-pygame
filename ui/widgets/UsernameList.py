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

            text = player.username
            
            # Draw text to screen
            font = pygame.font.SysFont("arial", 25)

            # If it's the player's turn, highlight their name red
            if player.playerTurn:
                textColor = (255, 0, 0)

            # Else if it's the player's turn to bid, highlight their name blue
            elif player.playerBidTurn and game.isBiddingStage():
                textColor = (0, 0, 255)

            # Else, draw the username white
            else:
                textColor = (0, 0, 0)

            # Add the player bid to the text if they've bid
            if player.playerBid is not None:
                text = player.username + " -> " + str(player.playerBid)

            text = font.render(text, 1, textColor)
            screen.blit(text, (0, (y * player.id)))
