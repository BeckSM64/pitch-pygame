import random


class SCard:
    def __init__(self, value, suit):

        # Set card suit and value
        self.value = value
        self.suit = suit


class SHand:
    def __init__(self, cards):
        self.cards = cards

    def size(self):
        return len(self.cards)


class SDeck:
    def __init__(self):

        # Holds 52 cards
        self.deck = []

        suit = ""

        # Add cards to the deck
        for i in range(4):
            for j in range(2, 15):
                if i == 0:
                    suit = "spades"
                elif i == 1:
                    suit = "clubs"
                elif i == 2:
                    suit = "hearts"
                else:
                    suit = "diamonds"

                # Add the card to the deck with
                # the appropriate value and suit
                self.deck.append(SCard(j, suit))

    def shuffle(self):

        # Shuffle the deck
        random.shuffle(self.deck)

    def deal_hand(self):

        hand = []
        for i in range(6):
            hand.append(self.deck[i])

        del self.deck[:6]

        return SHand(hand)


class SMainPile:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def size(self):
        return len(self.cards)

    def isBestCard(self, cardToCompare, trump):

        # If the pile has a trump card in it
        if self.hasTrump(trump):

            # If card played was non trump, it's not the best card in the pile
            if cardToCompare.suit != trump:
                return False

            else:

                # Check if there is a greater trump card in the pile
                for card in self.cards:
                    if (card.value > cardToCompare.value) and (card.suit == trump):
                        return False
                return True

        else:

            # Get the current suit for the pile
            baseSuit = self.cards[0].suit

            # If the card played isn't the current suit or trump,
            # cannot be the best card
            if cardToCompare.suit != baseSuit:
                return False

            else:
                for card in self.cards:

                    # If card is same suit as player card and value is greater,
                    # player did not play the best card
                    if (card.value > cardToCompare.value) and (
                        card.suit == cardToCompare.suit
                    ):
                        return False

                return True

    def hasTrump(self, trump):
        for card in self.cards:
            if card.suit == trump:
                return True
        return False

    def hasJack(self, trump):
        for card in self.cards:
            if card.value == 11 and card.suit == trump:
                return True
        return False

    def hasJick(self, trump):

        # Determine jick suit based on trump (Opposite same colored suit)
        jickSuit = None
        if trump == "hearts":
            jickSuit = "diamonds"
        elif trump == "diamonds":
            jickSuit = "hearts"
        elif trump == "spades":
            jickSuit = "clubs"
        else:
            jickSuit = "spades"

        # Check if player has jick
        for card in self.cards:
            if card.value == 11 and card.suit == jickSuit:
                return True
        return False

    def getHigh(self, trump):

        # If there is no trump card, can't have potential high
        if not self.hasTrump(trump):
            return None

        highCard = SCard(2, trump)  # High card will always be greater than this
        for card in self.cards:
            if card.value > highCard.value and card.suit == trump:
                highCard = card
        return highCard

    def getLow(self, trump):

        # If there is no trump card, can't have potential high
        if not self.hasTrump(trump):
            return None

        lowCard = SCard(14, trump)  # High card will always be greater than this
        for card in self.cards:
            if card.value < lowCard.value and card.suit == trump:
                lowCard = card
        return lowCard

    def getGame(self):

        gameScore = 0
        for card in self.cards:

            if card.value == 10:
                gameScore += 10
            elif card.value == 11:
                gameScore += 1
            elif card.value == 12:
                gameScore += 2
            elif card.value == 13:
                gameScore += 3
            elif card.value == 14:
                gameScore += 4

        return gameScore


class Player:
    def __init__(self, id, hand, conn):

        self.playerHand = hand
        self.playerWent = False
        self.playerBid = None
        self.playerTurn = False
        self.ready = False
        self.id = id
        self.conn = None
        self.username = None
        self.wonCards = SMainPile()
        self.score = 0
        self.roundPoints = 0

        # Make player 0 bid first by default
        if self.id == 0:
            self.playerBidTurn = True
        else:
            self.playerBidTurn = False
