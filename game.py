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

        # Setup game logic
        self.trump = None

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

    def isHandsEmpty(self):
        for player in self.players:
            if player.playerHand.size() != 0:
                return False
        return True

    def isPlayersReady(self):
        for player in self.players:
            if player.ready:
                return True
        return False

    def determinePlayerTurn(self):
        for i in range(len(self.players)):
            if self.players[i].playerTurn == True:
                self.players[i].playerTurn = False
                if (i + 1) == len(self.players):
                    self.players[0].playerTurn = True
                else:
                    self.players[i + 1].playerTurn = True
                break
                
            