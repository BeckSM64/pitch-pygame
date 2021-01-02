import pygame
from pygame.locals import *
from Card import Card

class MainPile(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
    
    def add_card(self, card):

        # screen size for position calculations
        w, h = pygame.display.get_surface().get_size()

        self.add(card)

        # rotate card
        if len(self) == 1:
            card.set_pos((w / 2) - (Card.width / 2), (h / 2) - (Card.height / 2))
        elif len(self) == 2:
            card.set_pos((w / 2) - (Card.width / 2) - (Card.height / 5), (h / 2) - (Card.height / 2) - (Card.width / 3))
            card.rot_center(90)
        elif len(self) == 3:
            card.set_pos((w / 2) - (Card.width / 2), (h / 2) - (Card.height / 2) - (Card.height / 2))
            card.rot_center(180)
        else:
            card.set_pos((w / 2) - (Card.width / 2) + (Card.height / 5), (h / 2) - (Card.height / 2) - (Card.width / 3))
            card.rot_center(270)
    