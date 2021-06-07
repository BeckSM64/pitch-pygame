import pygame
from pygame.locals import *
from game.objects.Card import *
from resources.Resources import *
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

            # Get the cards the player one as a card collection
            wonCards = Resources.get_card_collection(player.wonCards)

            # Set the position of the cards to be drawn on the screen
            i = 0
            for card in wonCards:
                card.set_pos(x * player.id, 25 + ((Card.width * i) / 2))
                i += 1

            # Draw the cards to the screen
            wonCards.draw(screen)
