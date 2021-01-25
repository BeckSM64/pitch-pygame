import pygame
from pygame.locals import *
from Button import Button
from GameState import GameState

def titleScreen():

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

    # Start button
    startButton = Button(200, 50, (w / 2) - 100, (h / 2) - 25, (255, 255, 255), (0, 0, 0), "START")

    # Host game button
    hostButton = Button(200, 50, (w / 2) - 100, (h / 2) - 25, (255, 255, 255), (0, 0, 0), "HOST")

    # Join button
    joinButton = Button(200, 50, (w / 2) - 100, (h / 2) + 30, (255, 255, 255), (0, 0, 0), "JOIN")

    # Quit button
    quitButton = Button(200, 50, (w / 2) - 100, (h / 2) + 30, (255, 255, 255), (0, 0, 0), "QUIT")
    quitButton = Button(200, 50, (w / 2) - 100, (h / 2) + 85, (255, 255, 255), (0, 0, 0), "QUIT")

    run = True

    # Game loop
    while run:
        clock.tick(60)
        for event in pygame.event.get():

            # Check for quit event
            if event.type == QUIT:
                return GameState.QUIT

            # Check for click event
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: # the right mouse button
                        
                    # Check if host button was clicked
                    if hostButton.isClicked(event.pos):
                        return GameState.NEWGAME

                    # Check if join button was clicked
                    if joinButton.isClicked(event.pos):
                        return GameState.JOIN

                    # Check if quit button was clicked
                    if quitButton.isClicked(event.pos):
                        return GameState.QUIT

        # Draw buttons and stuff
        hostButton.draw(screen)
        joinButton.draw(screen)
        quitButton.draw(screen)

        pygame.display.flip()