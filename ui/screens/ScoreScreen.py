import pygame
from pygame.locals import *
from game.objects.Card import *
from resources.Resources import *
pygame.font.init()

class ScoreScreen:
    def __init__(self):

        # Screen width and height
        self.w, self.h = pygame.display.get_surface().get_size()

    def draw(self, game, screen):

        x = 200
        for player in game.players:

            text = player.username + ": " + str(player.score)

            # Create text
            font = pygame.font.SysFont("arial", 25)
            textColor = (0, 0, 0)
            textWidth, textHeight = font.size(text)
            text = font.render(text, 1, textColor)

            # Calculate x position of username text and cards
            posX = 0
            if game.numPlayers == 3:
                if player.id == 0:
                    posX = ((((self.w / 2) - (textWidth / 2)) / 2))
                elif player.id == 1:
                    posX = ((self.w / 2) - (textWidth / 2))
                else:
                    posX = (((((self.w / 2) - (textWidth / 2)) + self.w) / 2))
            else:
                pass

            # Draw text to screen
            screen.blit(text, (posX, 0))

            # Get the cards the player one as a card collection
            wonCards = Resources.get_card_collection(player.wonCards)

            # Set the position of the cards to be drawn on the screen
            i = 0
            for card in wonCards:
                card.set_pos((posX), 25 + ((Card.width * i) / 2))
                i += 1

            # Draw the cards to the screen
            wonCards.draw(screen)
