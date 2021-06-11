from network.ServerData import *

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

        # Keeps track of whose turn it is to bid at the start
        # of each round (player 0 by default)
        self.firstBidder = 0

        self.bidWinner = None

    def connected(self):
        return self.ready

    def winner(self):
        pass

    def resetWent(self):
        for player in self.players:
            player.playerWent = False

    def dealHand(self):
        return self.deck.deal_hand()

    def dealHandWithPlayerId(self, playerId):
        self.players[playerId].playerHand = self.deck.deal_hand()

    def dealHands(self):
        for player in self.players:
            player.playerHand = self.deck.deal_hand()

    def newPlayer(self, id, conn):
        self.players.append(Player(id, self.dealHand(), conn))

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

        # If trick is over, reset player turns. Logic to determine
        # the winner of the trick will assign the next player turn
        if self.mainPile.size() % len(self.players) == 0:
            for player in self.players:
                player.playerTurn = False

        # Else, determine the next player turn
        else:
            for i in range(len(self.players)):
                if self.players[i].playerTurn == True:
                    self.players[i].playerTurn = False
                    if (i + 1) == len(self.players):
                        self.players[0].playerTurn = True
                    else:
                        self.players[i + 1].playerTurn = True
                    break

    def determineBidTurn(self):

        # Keep track of last player to bid
        lastBid = 0

        # Only update bid turn if currently in bidding stage
        if self.biddingStage:

            # Determine which player's turn it is to bid
            for i in range(len(self.players)):
                if self.players[i].playerBidTurn == True:
                    lastBid = i
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

                # Stuck with it
                self.players[lastBid].playerBid = 2
                playerIndex = lastBid
            
            # Set starting player turn
            self.players[playerIndex].playerTurn = True

            # Set bid winner
            self.bidWinner = playerIndex

    def determineFirstBidder(self):

        if (self.firstBidder + 1) == len(self.players):
            self.firstBidder = 0
        else:
            self.firstBidder += 1

        for player in self.players:
            if player.id == self.firstBidder:
                player.playerBidTurn = True
            else:
                player.playerBidTurn = False

    def didPlayersBid(self):
        for player in self.players:
            if player.playerBid is None:
                return False
        return True

    def getNumberOfBids(self):
        numBidders = 0
        for player in self.players:
            if player.playerBid is not None:
                numBidders += 1
        return numBidders

    def getHighestBid(self):
        highestBid = 0

        for player in self.players:
            if player.playerBid is not None and player.playerBid > highestBid:
                highestBid = player.playerBid
        return highestBid

    def isBiddingStage(self):
        return self.biddingStage

    def calculateScores(self):

        highCard  = SCard(2, self.trump)
        lowCard   = SCard(14, self.trump)
        gameScore = 0
        hasHigh   = None
        hasLow    = None
        hasGame   = None

        for player in self.players:

            # Determine jack point
            if player.wonCards.hasJack(self.trump):
                player.roundPoints += 1
                print(player.id, "has jack")

            # Determine high point
            playerCard = player.wonCards.getHigh(self.trump)
            if playerCard is not None:
                if playerCard.value > highCard.value:
                    highCard = playerCard
                    hasHigh = player.id

            # Determine low point
            playerCard = player.wonCards.getLow(self.trump)
            if playerCard is not None:
                if playerCard.value < lowCard.value:
                    lowCard = playerCard
                    hasLow = player.id

            # Determine game point
            playerScore = player.wonCards.getGame()
            if playerScore > gameScore:
                gameScore = playerScore
                hasGame = player.id

        # Check if two players had the high game score
        # If so, no game point
        for player in self.players:
            if player.wonCards.getGame() == gameScore and player.id != hasGame:
                hasGame = None

        # Award points
        for player in self.players:

            # Award high
            if hasHigh == player.id:
                player.roundPoints += 1
                print(player.id, "has high", highCard.value, "of", highCard.suit)

            # Award low
            if hasLow == player.id:
                player.roundPoints += 1
                print(player.id, "has low", lowCard.value, "of", lowCard.suit)

            # Award game point
            if hasGame == player.id:
                player.roundPoints += 1
                print(player.id, "has game", gameScore)

        # Print player scores
        for player in self.players:
            if player.id == self.bidWinner:
                if player.roundPoints >= player.playerBid:
                    player.score += player.roundPoints
                else:
                    player.score -= player.playerBid
            else:
                player.score += player.roundPoints
            print("PLAYER", player.id, "SCORE:", player.score)
