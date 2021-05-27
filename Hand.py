import pygame
from pygame.locals import *
from Card import Card

class Hand(pygame.sprite.Group):
    def __init__(self, cards):

        # Super class constructor
        pygame.sprite.Group.__init__(self)

        # Set card positions
        w, h = pygame.display.get_surface().get_size()
        cards[0].set_pos((w / 2) - (Card.width * 3), (h - Card.height))
        cards[1].set_pos((w / 2) - (Card.width * 2), (h - Card.height))
        cards[2].set_pos((w / 2) - (Card.width), (h - Card.height))
        cards[3].set_pos((w / 2), (h - Card.height))
        cards[4].set_pos((w / 2) + (Card.width), (h - Card.height))
        cards[5].set_pos((w / 2) + (Card.width * 2), (h - Card.height))

        # Add cards to hand
        for i in range(6):
            self.add(cards[i])

    
    def hasCurrentSuit(self, currentSuit):
        for card in self:
            if card.suit == currentSuit:
                return True
        return False
