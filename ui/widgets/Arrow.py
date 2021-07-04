import pygame
from pygame.locals import *
import resources.Resources as Resources

class Arrow(pygame.sprite.Sprite):

    width  = 50
    height = 50

    def __init__(self, x, y, rotation = None):

        # Super class constructor
        pygame.sprite.Sprite.__init__(self)

        # Load card image and create sprite
        filename = f"arrow.png"
        self.image, self.rect = Resources.load_png(filename)
        self.screen = pygame.display.get_surface()
        self.image = pygame.transform.smoothscale(self.image, (Arrow.width, Arrow.height))
        self.area = self.screen.get_rect()
        self.sprite = pygame.sprite.RenderPlain(self)
        self.rect = self.image.get_rect()

        # Set position of trump image
        self.rect.x = x
        self.rect.y = y

        # Rotate image if rotation was specified
        if rotation is not None:
            rot_image  = pygame.transform.rotate(self.image, rotation)
            rot_rect   = rot_image.get_rect(center=self.rect.center)
            self.image = rot_image
            self.rect  = rot_rect

    def isClicked(self, eventPos):
        return self.rect.collidepoint(eventPos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
