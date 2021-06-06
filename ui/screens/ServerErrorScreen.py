import pygame
from pygame.locals import *
from ui.widgets.Button import Button
from game.logic.GameState import GameState
from ui.widgets.TextBox import TextBox
pygame.font.init()

def serverErrorScreen():

    # Clock
    clock = pygame.time.Clock()

    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
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

    # Back button
    mainMenuButton = Button(200, 50, (w / 2) - 100, (h / 2) - 25, (255, 255, 255), (0, 0, 0), "MAIN MENU")

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

                    # Check if back button was clicked
                    if mainMenuButton.isClicked(event.pos):
                        return GameState.TITLE
    
        # Blit the background of the screen
        screen.blit(background, (0, 0))
        
        # Draw buttons and stuff
        mainMenuButton.draw(screen)
        displayError(screen, w, h)

        pygame.display.flip()

def displayError(screen, w, h):

    # Draw text to screen
    font = pygame.font.SysFont("arial", 25)
    textColor = (255, 0, 0)
    text = "Error Connecting to Server"
    textWidth, textHeight = font.size(text)
    text = font.render(text, 1, textColor)
    screen.blit(text, ((w / 2) - (textWidth / 2), (h / 2) - 100))
