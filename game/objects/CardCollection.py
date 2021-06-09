import pygame
from pygame.locals import *
from game.objects.Card import Card

class CardCollection(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
    
    def add_card(self, card):

        # Add card to list
        self.add(card)
    