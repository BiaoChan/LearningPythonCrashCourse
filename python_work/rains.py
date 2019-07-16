import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group
from random import randint

class Settings():
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 1000

        self.rain_width = 1
        self.rain_height = 15
        self.rain_drop_speed = 8
        self.rain_color = (60, 60, 60)

        self.wind_speed = 0

        self.flat_width = 249
        self.flat_height = 3
        self.flat_move_speed = 3
        self.flat_color = (60, 60, 60)

class Flat():
    def __init__(self, screen, settings):
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, settings.flat_width, settings.flat_height)
        self.rect.center = self.screen_rect.center
        self.color = settings.flat_color
        self.move_left = False
        self.move_right = False
        self.move_speed = settings.flat_move_speed
        self.x = float(self.rect.x)


    def update(self, rains):
        if self.move_left and self.rect.left >= self.screen_rect.left:
            self.x -= self.move_speed
        if self.move_right and self.rect.right <= self.screen_rect.right:
            self.x += self.move_speed
        self.rect.x = self.x

        collisions = pygame.sprite.spritecollide(self, rains, True)

    def draw_flat(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Rain(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, settings.rain_width, settings.rain_height)
        self.drop_speed = settings.rain_drop_speed
        self.wind_speed = settings.wind_speed
        self.color = settings.rain_color
        self.rect.bottom = self.screen_rect.top
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def draw_rain(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        self.y += self.drop_speed
        self.x += self.wind_speed
        self.rect.y = self.y
        self.rect.x = self.x


def check_event(flat):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_RIGHT:
                flat.move_right = True
            elif event.key == pygame.K_LEFT:
                flat.move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                flat.move_right = False
            elif event.key == pygame.K_LEFT:
                flat.move_left = False

def create_rain(screen, settings, rains):
    rain = Rain(screen, settings)
    rain.rect.x = randint(0, settings.screen_width-settings.rain_width)
    rain.x = float(rain.rect.x)
    rains.add(rain)

def raining():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,
        settings.screen_height))
    rains = Group()
    flat = Flat(screen, settings)
    while True:
        check_event(flat)
        for num in range(2):
            create_rain(screen, settings, rains)
        screen.fill((67, 170, 200))
        rains.update()
        flat.update(rains)
        flat.draw_flat()
        for rain in rains.sprites().copy():
            if rain.rect.top >= rain.screen_rect.bottom:
                rains.remove(rain)
            rain.draw_rain()
        pygame.display.flip()

raining()
