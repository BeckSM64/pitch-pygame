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

        # Flag to determine if in bidding stage or not
        self.biddingStage = True

        # Setup game logic
        self.trump = None
        self.currentSuit = None

        # Shows who is currently winning the trick
        self.winningTrick = None

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

    def determineBidTurn(self):

        # Only update bid turn if currently in bidding stage
        if self.biddingStage:

            # Determine which player's turn it is to bid
            for i in range(len(self.players)):
                if self.players[i].playerBidTurn == True:
                    self.players[i].playerBidTurn = False
                    if (i + 1) == len(self.players):
                        self.players[0].playerBidTurn = True
                    else:
                        self.players[i + 1].playerBidTurn = True
                    break
        
        # Determine if all players have bid
        self.biddingStage = False
        for player in self.players:
            if player.playerBid is None:
                self.biddingStage = True

        # Determine who won bid if bidding stage is over
        if not self.biddingStage:
            highestBid = 0
            playerIndex = 0
            for i in range(len(self.players)):
                if self.players[i].playerBid > highestBid:
                    highestBid = self.players[i].playerBid
                    playerIndex = i

            # Check if everyone passed and someone is stuck with 2 bid
            if highestBid == 0:
                highestBid = 2
                
                # Person stuck with it is to left of first bidder
                if playerIndex - 1 < 0:
                    playerIndex = len(self.players) - 1
                else:
                    playerIndex = playerIndex - 1
                
                # Set player bid to two
                self.players[playerIndex].playerBid = 2
            
            # Set starting player turn
            self.players[playerIndex].playerTurn = True

    def didPlayersBid(self):
        for player in self.players:
            if player.playerBid is None:
                return False
        return True
            