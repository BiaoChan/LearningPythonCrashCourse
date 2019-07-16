import pygame
from pygame.sprite import Sprite
from random import randint

class Acorn(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.image = pygame.image.load('images/acorn1.png')
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        self.rect.left = randint(0, settings.screen_width - self.rect.width)
        self.rect.bottom = self.screen_rect.top
        self.y = float(self.rect.y)

    def update(self, acorns):
        if self.rect.top >= self.screen_rect.bottom:
            acorns.remove(self)

        self.y += self.settings.acorn_drop_speed
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
