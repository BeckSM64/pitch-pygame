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

class Player:
    def __init__(self, id, hand):

        self.playerHand = hand
        self.playerWent = False
        self.playerBid = None
        self.playerTurn = False
        self.ready = False
        self.id = id

        # Make player 0 bid first by default
        if self.id == 0:
            self.playerBidTurn = True
        else:
            self.playerBidTurn = False
