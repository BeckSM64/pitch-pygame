import random

class SCard:
    def __init__(self, value, suit):

        # Set card suit and value
        self.value = value
        self.suit = suit

class SHand:
    def __init__(self, cards):
        self.cards = cards

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
                elif i == 3:
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
            print(self.deck[i].value, self.deck[i].suit)
            hand.append(self.deck[i])
        
        del self.deck[:6]

        return SHand(hand)

