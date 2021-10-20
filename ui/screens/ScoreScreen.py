import pygame
from pygame.locals import *
from game.objects.Card import *
from resources.Resources import *
import resources.Resources as Resources

pygame.font.init()


class ScoreScreen:
    def __init__(self):

        # Screen width and height
        self.w, self.h = pygame.display.get_surface().get_size()

    def draw(self, game, screen):

        if game.maxPlayers == 3:
            self.drawPlayerNamesAndCards(screen, game, 3)
        else:
            self.drawPlayerNamesAndCards(screen, game, 2)

    def drawPlayerNamesAndCards(self, screen, game, numPlayers):
        for i in range(numPlayers):

            if numPlayers == 3:
                text = game.players[i].username + ": " + str(game.players[i].score)
            else:
                text = (
                    game.players[i].username
                    + "/"
                    + game.players[i + 2].username
                    + ": "
                    + str(game.players[i].score)
                )

            # Create text
            textColor = (0, 0, 0)
            textWidth, textHeight = Resources.FONT_VARIABLE_SIZE.size(text)
            text = Resources.FONT_VARIABLE_SIZE.render(text, 1, textColor)

            # Calculate x position of username text and cards
            if numPlayers == 3:
                posX = self.calculateXPosition(game.numPlayers + 1, i, textWidth)
            else:
                posX = self.calculateXPosition(game.numPlayers - 1, i, textWidth)

            # Draw text to screen
            screen.blit(text, (posX, 0))

            # Get the cards the player won as a card collection
            if numPlayers == 3:
                wonCards = Resources.get_card_collection(game.players[i].wonCards)
            else:
                wonCards = Resources.combine_card_collections(
                    Resources.get_card_collection(game.players[i].wonCards),
                    Resources.get_card_collection(game.players[i + 2].wonCards),
                )

            # Set the position of the cards to be drawn on the screen
            # TODO: Look into not doing this every frame
            i = 0
            for card in wonCards:
                card.set_size(
                    Resources.SCALABLE_CARD_WIDTH, Resources.SCALABLE_CARD_HEIGHT
                )
                card.set_pos(
                    posX + ((textWidth / 2) - (Resources.SCALABLE_CARD_WIDTH / 2)),
                    25 + ((Resources.SCALABLE_CARD_WIDTH * i) / 2),
                )
                i += 1

            # Draw the cards to the screen
            wonCards.draw(screen)

        # Draw ten and under pile
        text = "Ten and Under Pile"

        # Create text with specified font
        textColor = (0, 0, 0)
        textWidth, textHeight = Resources.FONT_VARIABLE_SIZE.size(text)
        text = Resources.FONT_VARIABLE_SIZE.render(text, 1, textColor)

        if game.maxPlayers == 3:
            # Calculate x position of tend and under text and cards
            posX = self.calculateXPosition(
                game.numPlayers + 1, game.numPlayers, textWidth
            )
        else:
            # Calculate x position of tend and under text and cards
            posX = self.calculateXPosition(game.numPlayers - 1, 2, textWidth)

        # Draw text to screen
        screen.blit(text, (posX, 0))

        # Get the ten and under cards as a card collection
        tenAndUnderCollection = Resources.get_card_collection(
            game.tenAndUnderCollection
        )

        # Set the position of the cards to be drawn on the screen
        i = 0
        for card in tenAndUnderCollection:
            card.set_size(Resources.SCALABLE_CARD_WIDTH, Resources.SCALABLE_CARD_HEIGHT)
            card.set_pos(
                posX + ((textWidth / 2) - (Resources.SCALABLE_CARD_WIDTH / 2)),
                25 + ((Resources.SCALABLE_CARD_WIDTH * i) / 2),
            )
            i += 1

        tenAndUnderCollection.draw(screen)

    def calculateXPosition(self, numPlayers, playerId, textWidth):
        posX = ((self.w / (numPlayers + 1)) * (playerId + 1)) - (textWidth / 2)
        return posX
