from ServerData import *

class Game:
    def __init__(self, id):

        # Setup game objects
        self.deck = SDeck()
        self.deck.shuffle()
        self.mainPile = SMainPile()

        self.p1Went = False
        self.p2Went = False
        self.p3Went = False
        self.p1Hand = self.dealHand()
        self.p2Hand = self.dealHand()
        self.p3Hand = self.dealHand()
        self.ready = False
        self.id = id

    def connected(self):
        return self.ready

    def winner(self):
        pass

    def resetWent(self):
        # self.p1Went = False
        # self.p2Went = False
        # self.p3Went = False
        pass

    def dealHand(self):
        return self.deck.deal_hand()

    def getHand(self, player):
        if player == 0:
            return self.p1Hand
        elif player == 1:
            return self.p2Hand
        else:
            return self.p3Hand