import pygame
from pygame.locals import *
from Card import Card

class MainPile(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
    
    def add_card(self, card):
        w, h = pygame.display.get_surface().get_size()
        card.set_pos((w / 2) - (Card.width / 2), (h / 2) - (Card.height / 2))
        self.add(card)
    