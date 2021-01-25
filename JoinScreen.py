import pygame
from pygame.locals import *
from Button import Button
from TextBox import TextBox
from GameState import GameState

def joinScreen():

    # Clock
    clock = pygame.time.Clock()

    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode((450, 500))
    pygame.display.set_caption('Pitch')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 250, 250))

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # screen size for position calculations
    w, h = pygame.display.get_surface().get_size()

    # Join button
    joinButton = Button(200, 50, (w / 2) - 100, (h / 2) -25, (255, 255, 255), (0, 0, 0), "JOIN")

    # Text box for game hash
    textBox = TextBox((w / 2) - 100, (h / 2) -80, 200, 50)

    run = True

    # Game loop
    while run:
        clock.tick(60)

        for event in pygame.event.get():

            # Check if text box was interacted with
            textBox.handle_event(event)

            # Check for quit event
            if event.type == QUIT:
                return GameState.QUIT

            # Check for click event
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: # the right mouse button

                    # Check if host button was clicked
                    if joinButton.isClicked(event.pos):
                        print(textBox.text)
                        return GameState.NEWGAME, textBox.text

        # Draw buttons and stuff
        joinButton.draw(screen)
        textBox.draw(screen)

        pygame.display.flip()
