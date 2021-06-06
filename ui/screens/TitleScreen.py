import pygame
from pygame.locals import *
from Button import Button
from GameState import GameState
from TextBox import TextBox
pygame.font.init()

def titleScreen():

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

    # Start button
    startButton = Button(200, 50, (w / 2) - 100, (h / 2) - 25, (255, 255, 255), (0, 0, 0), "START")

    # Quit button
    quitButton = Button(200, 50, (w / 2) - 100, (h / 2) + 30, (255, 255, 255), (0, 0, 0), "QUIT")

    # Text botx to enter username
    textBox = TextBox((w / 2) - 100, (h / 2) - 80, 200, 50)

    run = True

    showError = False

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

                    # Check if start button was clicked
                    if startButton.isClicked(event.pos):
                        if len(textBox.text) == 0:
                            showError = True
                        else:
                            return GameState.NEWGAME, textBox.text # TODO: Look into if there's a better way to get this textbox input to the GameScreen other than returning the value here

                    # Check if quit button was clicked
                    if quitButton.isClicked(event.pos):
                        return GameState.QUIT

            # Proceed to game if enter is pressed in the textbox
            isInputEntered = textBox.handle_event(event)
            if isInputEntered and len(textBox.text) != 0:
                return GameState.NEWGAME, textBox.text
            elif isInputEntered and len(textBox.text) == 0:
                showError = True
    
        # Blit the background of the screen
        screen.blit(background, (0, 0))
        
        # Draw buttons and stuff
        startButton.draw(screen)
        quitButton.draw(screen)
        textBox.draw(screen)

        # Show error if username field is left blank
        if showError:
            displayInputError(screen, w, h)

        pygame.display.flip()

def displayInputError(screen, w, h):

    # Draw text to screen
    font = pygame.font.SysFont("arial", 15)
    textColor = (255, 0, 0)
    text = "*Username must not be blank"
    text = font.render(text, 1, textColor)
    screen.blit(text, ((w / 2) - 100, (h / 2) - 100))
