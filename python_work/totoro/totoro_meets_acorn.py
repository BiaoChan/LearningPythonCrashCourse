import pygame
import time
import sys
from pygame.sprite import Sprite, Group

from totoro import Totoro
from settings import Settings
from background import Background
from acorn import Acorn

def check_events(settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_LEFT:
                settings.totoro_move_left = True
            elif event.key == pygame.K_RIGHT:
                settings.totoro_move_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                settings.totoro_move_left = False
            elif event.key == pygame.K_RIGHT:
                settings.totoro_move_right = False

def create_acorn(acorns, screen, settings):
    acorn = Acorn(screen, settings)
    acorns.add(acorn)

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,
        settings.screen_height))
    bg = Background(screen)
    totoro = Totoro(screen, settings)
    acorns = Group()
    print(totoro.rect)
    while True:
        check_events(settings)

        create_acorn(acorns, screen, settings)

        screen.fill((0,0,0))
        bg.blitme()
        totoro.blitme()
        acorns.draw(screen)
        pygame.display.flip()

        totoro.update(acorns)
        acorns.update(acorns)

run_game()
