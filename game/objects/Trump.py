import pygame
from pygame.locals import *
import resources.Resources as Resources


class Trump(pygame.sprite.Sprite):
    def __init__(self, suit):

        # Super class constructor
        pygame.sprite.Sprite.__init__(self)

        # Set image width and height
        self.width = 50
        self.height = 50

        # Load card image and create sprite
        filename = f"suits/{suit}_hdpi.png"
        self.image, self.rect = Resources.load_png(filename)
        self.screen = pygame.display.get_surface()
        self.image = pygame.transform.smoothscale(self.image, (self.width, self.height))
        self.area = self.screen.get_rect()
        self.sprite = pygame.sprite.RenderPlain(self)
        self.rect = self.image.get_rect()

        # Screen width and height
        self.w, self.h = pygame.display.get_surface().get_size()

        # Set position of trump image
        self.rect.x = 0
        self.rect.y = self.h - self.rect.height

    def draw(self, screen):
        screen.blit(self.image, self.rect)
