import pygame
from pygame.locals import *
import os
from game.objects.Card import Card
from game.objects.Hand import Hand
from game.objects.MainPile import MainPile
from game.objects.CardCollection import CardCollection

# Screen size
SCREEN_WIDTH  = 896
SCREEN_HEIGHT = 504

def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join('resources', 'images', name)
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
        cards.append(Card(card.value, card.suit))

    # Make the new hand
    hand = Hand(cards)

    return hand

def get_main_pile(server_main_pile):
    """Convert server pile into main pile"""

    main_pile = MainPile()
    for card in server_main_pile.cards:
        card_for_pile = Card(card.value, card.suit)
        main_pile.add_card(card_for_pile)

    return main_pile

def get_card_collection(server_main_pile):
    """Convert server pile into card collection"""

    card_collection = CardCollection()
    for card in server_main_pile.cards:
        card_for_collection = Card(card.value, card.suit)
        card_collection.add_card(card_for_collection)

    return card_collection

def set_screen_size(width = 1280, height = 720):

    # Set global screen size variables
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    SCREEN_WIDTH  = width
    SCREEN_HEIGHT = height

    # Set screen size
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Pitch')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 250, 250))

    return screen, background
    