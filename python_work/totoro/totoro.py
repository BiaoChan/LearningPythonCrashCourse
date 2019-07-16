import pygame

class Totoro():
    def __init__(self, screen, settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.image_left = pygame.image.load('images/totoro_left.png')
        self.image_right = pygame.image.load('images/totoro_right.png')
        self.rect = self.image_right.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.x = float(self.rect.centerx)

    def blitme(self):
        if self.settings.totoro_image_direction == 'left':
            self.screen.blit(self.image_left, self.rect)
        elif self.settings.totoro_image_direction == 'right':
            self.screen.blit(self.image_right, self.rect)

    def update(self, acorns):
        if self.settings.totoro_move_left and self.rect.left >self.screen_rect.left:
            self.x -= self.settings.totoro_move_speed_factor
        if self.settings.totoro_move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.totoro_move_speed_factor

        self.rect.x = self.x

        if (self.settings.totoro_move_left and
                not self.settings.totoro_move_right):
            self.settings.totoro_image_direction = 'left'
        elif (not self.settings.totoro_move_left and
                self.settings.totoro_move_right):
            self.settings.totoro_image_direction = 'right'

        collision = pygame.sprite.spritecollide(self, acorns, True)
