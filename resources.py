import pygame
from pygame.locals import *
import os
from Card import Card
from Hand import Hand

def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join('images/cards', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print("Cannot load image:" + fullname)
        raise SystemExit(message)
    return image, image.get_rect()

def get_hand(server_hand):
    """Convert server hand to hand of cards"""

    # Create each card from the server cards
    cards = []
    for card in server_hand.cards:
        print(card.value, card.suit)
        cards.append(Card(card.value, card.suit))

    # Make the new hand
    hand = Hand(cards)

    return hand
    