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
            posX = self.calculateXPosition(game.numPlayers, player.id, textWidth)

            # Draw text to screen
            screen.blit(text, (posX, 0))

            # Get the cards the player one as a card collection
            wonCards = Resources.get_card_collection(player.wonCards)

            # Set the position of the cards to be drawn on the screen
            i = 0
            for card in wonCards:
                card.set_pos(posX + ((textWidth / 2) - (Card.width / 2)), 25 + ((Card.width * i) / 2))
                i += 1

            # Draw the cards to the screen
            wonCards.draw(screen)

    def calculateXPosition(self, numPlayers, playerId, textWidth):
        posX = (((self.w / (numPlayers + 1)) * (playerId + 1)) - (textWidth / 2))
        return posX
