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

        # Draw player names, scores, and cards
        if game.maxPlayers == 3:
            self.drawPlayerNamesAndCards(screen, game, 3)
        else:
            self.drawPlayerNamesAndCards(screen, game, 2)

        # Draw high, low, jack, and game indicators
        self.drawHighLowJackJickStatus(screen, game)

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

    def drawHighLowJackJickStatus(self, screen, game):

        # Get the highest and lowest cards played so far
        highCard = game.getHighestCard()
        lowCard = game.getLowestCard()

        # Get the username of who has the jack (if anyone)
        userWithJack = game.getUsernameWithJack()

        # Get the username of who has the jick (if anyone)
        userWithJick = game.getUsernameWithJick()

        # Setup strings for indicator display
        if len(userWithJack) == 0:
            userWithJack = " - "

        if len(userWithJick) == 0:
            userWithJick = " - "

        if highCard is not None:
            highCard = highCard.getCardAsString()
        else:
            highCard = ""
        
        if lowCard is not None:
            lowCard = lowCard.getCardAsString()
        else:
            lowCard = ""
        
        # High, low, jack, game indicators
        highText = "HIGH: " + game.getUsernameWithHigh() + " - " + highCard
        lowText = "LOW: " + game.getUsernameWithLow() + " - " + lowCard
        jackText = "JACK: " + userWithJack
        jickText = "JICK: " + userWithJick

        # Create text color
        textColor = (0, 0, 0)

        # High text
        highTextWidth, highTextHeight = Resources.FONT_VARIABLE_SIZE.size(highText)
        highText = Resources.FONT_VARIABLE_SIZE.render(highText, 1, textColor)

        # Low text
        lowTextWidth, lowTextHeight = Resources.FONT_VARIABLE_SIZE.size(lowText)
        lowText = Resources.FONT_VARIABLE_SIZE.render(lowText, 1, textColor)

        # Jack text
        jackTextWidth, jackTextHeight = Resources.FONT_VARIABLE_SIZE.size(jackText)
        jackText = Resources.FONT_VARIABLE_SIZE.render(jackText, 1, textColor)

        # Jick text
        jickTextWidth, jickTextHeight = Resources.FONT_VARIABLE_SIZE.size(jickText)
        jickText = Resources.FONT_VARIABLE_SIZE.render(jickText, 1, textColor)

        # Calculate x position of text
        # TODO: Fix magic numbers
        if game.gameMode == "Normal":
            numPoints = 3
        elif game.gameMode == "Jick":
            numPoints = 4
            
        highPosX = self.calculateXPosition(numPoints, 0, highTextWidth)
        lowPosX = self.calculateXPosition(numPoints, 1, lowTextWidth)
        jackPosX = self.calculateXPosition(numPoints, 2, jackTextWidth)
        jickPosX = self.calculateXPosition(numPoints, 3, jickTextWidth)

        # Draw text to screen
        screen.blit(highText, (highPosX, (Resources.SCREEN_HEIGHT - highTextHeight)))
        screen.blit(lowText, (lowPosX, (Resources.SCREEN_HEIGHT - lowTextHeight)))
        screen.blit(jackText, (jackPosX, (Resources.SCREEN_HEIGHT - jackTextHeight)))

        if game.gameMode == "Jick":
            screen.blit(jickText, (jickPosX, (Resources.SCREEN_HEIGHT - jickTextHeight)))

    def calculateXPosition(self, numPlayers, playerId, textWidth):
        posX = ((self.w / (numPlayers + 1)) * (playerId + 1)) - (textWidth / 2)
        return posX
