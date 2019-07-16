import pygame
import time

class Fps():
    # def __init__(self):

    #

    #
    # def show_fps(self):

    def __init__(self, screen):

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.COUNT = pygame.USEREVENT + 1
        self.update_time = 200
        pygame.time.set_timer(self.COUNT, self.update_time)

        self.fps = 0
        self.frames = 0
        self.last_time = time.time()

        self.prep_fps()

    def show_fps(self):
        self.screen.blit(self.image, self.rect)

    def prep_fps(self):
        self.str = "fps: " + str(round(self.fps, 2))
        self.image = self.font.render(self.str, True, self.text_color)
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.bottom = self.screen_rect.bottom - 10

    def update_fps(self):
        now_time = time.time()
        if now_time != self.last_time:
            self.fps = self.frames / (now_time-self.last_time)
        self.frames = 0
        self.last_time = now_time
        self.prep_fps()
