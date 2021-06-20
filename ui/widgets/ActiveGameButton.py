from ui.widgets.Button import Button

class ActiveGameButton(Button):
    def __init__(self, game, width, height, x, y, color, textColor):

        buttonText = game.gameName + " - " + str(game.numPlayers)
        self.gameName = game.gameName

        # Call button constructor
        Button.__init__(self, width, height, x, y, color, textColor, buttonText)
        