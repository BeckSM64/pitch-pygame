import pygame
from pygame.locals import *
import resources.Resources as Resources


class Card(pygame.sprite.Sprite):

    # Size of card
    width = 75
    height = 125

    def __init__(self, value, suit):

        # Super class constructor
        pygame.sprite.Sprite.__init__(self)

        # Set card suit and value
        self.value = value
        self.suit = suit

        card_value_name = value
        if value == 11:
            card_value_name = "jack"
        if value == 12:
            card_value_name = "queen"
        if value == 13:
            card_value_name = "king"
        if value == 14:
            card_value_name = "ace"

        # Load card image and create sprite
        filename = f"cards/{card_value_name}_of_{suit}.png"
        self.image, self.rect = Resources.load_png(filename)
        self.screen = pygame.display.get_surface()
        self.image = pygame.transform.smoothscale(self.image, (Card.width, Card.height))
        self.area = self.screen.get_rect()
        self.sprite = pygame.sprite.RenderPlain(self)
        self.rect = self.image.get_rect()

    def set_size(self, width, height):
        self.image = pygame.transform.smoothscale(self.image, (width, height))
        self.area = self.screen.get_rect()
        self.sprite = pygame.sprite.RenderPlain(self)
        self.rect = self.image.get_rect()

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def get_pos_x(self):
        return self.rect.x

    def get_pos_y(self):
        return self.rect.y

    def rot_center(self, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(self.image, angle)
        rot_rect = rot_image.get_rect(center=self.rect.center)
        self.image = rot_image
        self.rect = rot_rect

    def isPlayable(self, game, handHasCurrentSuit):

        if (
            game.trump == self.suit
            or game.currentSuit == self.suit
            or game.mainPile.size() == 0
            or not handHasCurrentSuit
        ):
            return True
        else:
            return False
