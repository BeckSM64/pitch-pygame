import pygame
from pygame import display
from pygame.locals import *
from ui.widgets.Button import Button
from game.logic.GameState import GameState
from ui.widgets.TextBox import TextBox
import resources.Resources as Resources
pygame.font.init()

def videoSettingsScreen():

    # Clock
    clock = pygame.time.Clock()

    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode((Resources.SCREEN_WIDTH, Resources.SCREEN_HEIGHT))
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

    # 504p button
    fiveOFourButton = Button(200, 50, (w / 2) - 100, (h / 2) - 135, (255, 255, 255), (0, 0, 0), "896 x 504")

    # 648p button
    sixFourtyEightButton = Button(200, 50, (w / 2) - 100, (h / 2) - 80, (255, 255, 255), (0, 0, 0), "1152 x 648")

    # 720p button
    sevenTwentyButton = Button(200, 50, (w / 2) - 100, (h / 2) - 25, (255, 255, 255), (0, 0, 0), "1280 x 720")

    # Back button
    mainMenuButton = Button(200, 50, (w / 2) - 100, (h / 2) + 30, (255, 255, 255), (0, 0, 0), "MAIN MENU")

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

                    # Check if the 504p button was clicked
                    if fiveOFourButton.isClicked(event.pos):
                        screen, background = Resources.set_screen_size(896, 504)
                        Resources.set_ui_font_size(15)
                        Resources.set_scalable_card_size(50, 83)
                        fiveOFourButton, sixFourtyEightButton, sevenTwentyButton, mainMenuButton = updateUi(Resources.SCREEN_WIDTH, Resources.SCREEN_HEIGHT)

                    # Check if the 648p button was clicked
                    if sixFourtyEightButton.isClicked(event.pos):
                        screen, background = Resources.set_screen_size(1152, 648)
                        Resources.set_ui_font_size(20)
                        Resources.set_scalable_card_size(63, 105)
                        fiveOFourButton, sixFourtyEightButton, sevenTwentyButton, mainMenuButton = updateUi(Resources.SCREEN_WIDTH, Resources.SCREEN_HEIGHT)

                    # Check if the 720p button was clicked
                    if sevenTwentyButton.isClicked(event.pos):
                        screen, background = Resources.set_screen_size(1280, 720)
                        Resources.set_ui_font_size(23)
                        Resources.set_scalable_card_size(75, 125)
                        fiveOFourButton, sixFourtyEightButton, sevenTwentyButton, mainMenuButton = updateUi(Resources.SCREEN_WIDTH, Resources.SCREEN_HEIGHT)

                    # Check if back button was clicked
                    if mainMenuButton.isClicked(event.pos):
                        return GameState.TITLE
    
        # Blit the background of the screen
        screen.blit(background, (0, 0))
        
        # Draw buttons and stuff
        fiveOFourButton.draw(screen)
        sixFourtyEightButton.draw(screen)
        sevenTwentyButton.draw(screen)
        mainMenuButton.draw(screen)
        displayTitle(screen, Resources.SCREEN_WIDTH, Resources.SCREEN_HEIGHT)

        pygame.display.flip()

def displayTitle(screen, w, h):

    # Draw text to screen
    font = pygame.font.SysFont("arial", 25)
    textColor = (0, 0, 0)
    text = "VIDEO SETTINGS"
    textWidth, textHeight = font.size(text)
    text = font.render(text, 1, textColor)
    screen.blit(text, ((w / 2) - (textWidth / 2), 0))

def updateUi(screenWidth, screenHeight):
    
    fiveOFourButton      = Button(200, 50, (screenWidth / 2) - 100, (screenHeight / 2) - 135, (255, 255, 255), (0, 0, 0), "896 x 504")
    sixFourtyEightButton = Button(200, 50, (screenWidth / 2) - 100, (screenHeight / 2) - 80, (255, 255, 255), (0, 0, 0), "1152 x 648")
    sevenTwentyButton    = Button(200, 50, (screenWidth / 2) - 100, (screenHeight / 2) - 25, (255, 255, 255), (0, 0, 0), "1280 x 720")
    mainMenuButton       = Button(200, 50, (screenWidth / 2) - 100, (screenHeight / 2) + 30, (255, 255, 255), (0, 0, 0), "MAIN MENU")

    return fiveOFourButton, sixFourtyEightButton, sevenTwentyButton, mainMenuButton
