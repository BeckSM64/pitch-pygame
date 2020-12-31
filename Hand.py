import pygame
from pygame.locals import *
from Card import Card

class Hand(pygame.sprite.Group):
    def __init__(self, cards):

        # Super class constructor
        pygame.sprite.Group.__init__(self)

        # Loop through cards in hand
        for i in range(6):

            # Set position of cards in hand
            w, h = pygame.display.get_surface().get_size()
            cards[i].set_pos((i * 75), (h - Card.height))
            self.add(cards[i])
    
    def hasCurrentSuit(self, currentSuit):
        for card in self:
            if card.suit == currentSuit:
                return True
        return False
