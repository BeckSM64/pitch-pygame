import pygame
from pygame.locals import *
from ui.widgets.Button import Button


class ActiveGameButton(Button):
    def __init__(self, game, width, height, x, y, color, textColor):

        buttonText = (
            "Game Name: "
            + game.gameName
            + "\n"
            + "Open Slots: "
            + str(game.maxPlayers - game.numPlayers)
            + "\n"
            + "Game Mode: "
            + game.gameMode
        )
        self.gameName = game.gameName
        self.gameId = game.id

        # Call button constructor
        Button.__init__(self, width, height, x, y, color, textColor, buttonText)

    def setPos(self, x, y):

        # Update x and y position
        self.x = x
        self.y = y

        # Recreate rectangle
        self.rect = Rect(self.x, self.y, self.width, self.height)
