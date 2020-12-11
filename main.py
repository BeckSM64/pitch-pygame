import pygame
from pygame.locals import *
import os
import resources
from Card import Card
from Hand import Hand
from Deck import Deck
from MainPile import MainPile

def main():

    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Pitch')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 250, 250))

    # Initialize test deck
    test_deck = Deck()
    test_deck.shuffle()

    # Initialize test hand
    test_hand = Hand(test_deck.deal_hand())

    # Initialize main pile to play cards into
    main_pile = MainPile()

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Game loop
    while 1:
        for event in pygame.event.get():

            # Check for quit event
            if event.type == QUIT:
                return

            # Check for click event
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: # the right mouse button
                    for card in test_hand:
                        if card.rect.collidepoint(event.pos):
                            main_pile.add_card(card)
                            test_hand.remove(card)

        # Blit the background of the screen
        screen.blit(background, (0, 0))

        # Draw the hand on the screen
        test_hand.draw(screen)

        # Draw the main pile to the screen
        main_pile.draw(screen)

        pygame.display.flip()

if __name__ == '__main__':
    main()
