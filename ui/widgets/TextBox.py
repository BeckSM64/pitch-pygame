import pygame
import resources.Resources as Resources
from pygame.locals import *

COLOR_INACTIVE = pygame.Color("lightskyblue3")
COLOR_ACTIVE = pygame.Color("dodgerblue2")


class TextBox:
    def __init__(self, x, y, width, height, text=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = Rect(x, y, width, height)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = Resources.FONT_TWENTY_FIVE.render(text, True, (0, 0, 0))
        self.active = False

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            # If the user clicked on the input_box rect
            if self.rect.collidepoint(event.pos):

                # Toggle the active variable
                self.active = not self.active
            else:
                self.active = False

            # Change the current color of the input box
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        if event.type == pygame.KEYDOWN:
            if self.active:

                if event.key == pygame.K_RETURN:

                    # Return true if enter is pressed
                    return True
                elif event.key == pygame.K_BACKSPACE:

                    # Remove one character from text in textbox
                    self.text = self.text[:-1]
                else:
                    # Don't exceed the length of the text box
                    if (self.txt_surface.get_width() + 10) < (self.rect.w - 10):
                        self.text += event.unicode

                # Re-render the text
                self.txt_surface = Resources.FONT_TWENTY_FIVE.render(
                    self.text, True, (0, 0, 0)
                )

    def draw(self, screen):

        # Draw textbox to screen
        pygame.draw.rect(screen, self.color, self.rect, border_radius=5)

        # Draw the text to the screen
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
