from ServerData import *

class Game:
    def __init__(self, id):

        # list of player objects
        self.players = []

        # Setup game objects
        self.deck = SDeck()
        self.deck.shuffle()
        self.mainPile = SMainPile()
        self.ready = False
        self.numPlayers = 0
        self.id = id

    def connected(self):
        return self.ready

    def winner(self):
        pass

    def resetWent(self):
        for player in self.players:
            player.playerWent = False

    def dealHand(self):
        return self.deck.deal_hand()

    def dealHands(self):
        for player in self.players:
            player.playerHand = self.deck.deal_hand()

    def newPlayer(self, id):
        self.players.append(Player(id, self.dealHand()))
            