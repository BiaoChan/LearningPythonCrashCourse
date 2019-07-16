import pygame
import sys
from pygame.sprite import Sprite, Group
from random import randint

class Star(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('star.jpg')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = self.screen_rect.left
        self.rect.y = self.screen_rect.top

    def blitme(self):
        self.screen.blit(self.image, self.rect)

def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def create_star(screen, set_x, set_y, stars = ''):
    star = Star(screen)
    star.rect.x = star.rect.width * set_x
    star.rect.y = star.rect.height * set_y
    stars.add(star)
    return star

def run_program():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))

    stars = Group()
    # for x in range(10):
    #     for y in range(10):
    #         create_star(screen, x, y, stars)
    while True:
        check_event()
        screen.fill((246,246,246))
        randx = randint(0,10)
        randy = randint(0,10)
        # star = create_star(screen, randx, randy)
        # star.blitme()
        create_star(screen, randx, randy, stars)
        stars.draw(screen)
        pygame.display.flip()
run_program()
