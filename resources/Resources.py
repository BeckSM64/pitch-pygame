import pygame
from pygame.locals import *
import os
from game.objects.Card import Card
from game.objects.Hand import Hand
from game.objects.MainPile import MainPile
from game.objects.CardCollection import CardCollection
pygame.init()

# Screen size
SCREEN_WIDTH  = 896
SCREEN_HEIGHT = 504

# UI Text Font Size
UI_TEXT_SIZE = 15

# Scalable Card Size
SCALABLE_CARD_WIDTH  = 50
SCALABLE_CARD_HEIGHT = 83

# Active font
ACTIVE_FONT = "arial"

# Video Settings
videoSettings = {
    504 : {"fontSize" : 15, "cardWidth" : 50, "cardHeight" : 83},
    648 : {"fontSize" : 20, "cardWidth" : 63, "cardHeight" : 105},
    720 : {"fontSize" : 23, "cardWidth" : 75, "cardHeight" : 125}
}

# Fonts
FONT_SIXTY         = pygame.font.SysFont(ACTIVE_FONT, 60)
FONT_TWENTY_FIVE   = pygame.font.SysFont(ACTIVE_FONT, 25)
FONT_THIRTY        = pygame.font.SysFont(ACTIVE_FONT, 30)
FONT_FIFTEEN       = pygame.font.SysFont(ACTIVE_FONT, 15)
FONT_VARIABLE_SIZE = pygame.font.SysFont(ACTIVE_FONT, UI_TEXT_SIZE)

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

def combine_card_collections(cardCollection1, cardCollection2):
    """Combine two card collections"""

    for card in cardCollection2:
        cardCollection1.add_card(card)

    return cardCollection1

def set_screen_size(width = 1280, height = 720):

    # Set global screen size variables
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    SCREEN_WIDTH  = width
    SCREEN_HEIGHT = height

    # Get settings from the settings dictionary based on screen size
    fontSize   = videoSettings[SCREEN_HEIGHT]["fontSize"]
    cardWidth  = videoSettings[SCREEN_HEIGHT]["cardWidth"]
    cardHeight = videoSettings[SCREEN_HEIGHT]["cardHeight"]

    # Resize all other elements
    set_ui_font_size(fontSize)
    set_scalable_card_size(cardWidth, cardHeight)

    # Set screen size
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Pitch')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((21, 107, 5))

    return screen, background

def set_ui_font_size(fontSize):

    # Set global ui font size and
    # font variable size variables
    global UI_TEXT_SIZE
    global FONT_VARIABLE_SIZE

    # Update UI text size and variable size font
    UI_TEXT_SIZE       = fontSize
    FONT_VARIABLE_SIZE = pygame.font.SysFont("arial", UI_TEXT_SIZE)

def set_scalable_card_size(cardWidth, cardHeight):

    # Set global scalable card size variables
    global SCALABLE_CARD_WIDTH
    global SCALABLE_CARD_HEIGHT

    SCALABLE_CARD_WIDTH  = cardWidth
    SCALABLE_CARD_HEIGHT = cardHeight
    