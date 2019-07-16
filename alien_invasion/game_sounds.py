import pygame

class GameSounds():
    def __init__(self):
        self.biu = pygame.mixer.Sound('sounds/biu.wav')
        self.bang = pygame.mixer.Sound('sounds/bang.wav')

    def shooting_sound(self):
        self.biu.play()

    def explosive_sound(self):
        self.bang.play()

# pygame.mixer.init()
# biu = pygame.mixer.Sound('sounds/biu.wav')
# biu.play()
# # bang = pygame.mixer.Sound('sounds/bang.wav')
# # bang.play()
# # pygame.mixer.music.load('sounds/therose.mp3')
# # pygame.mixer.music.play()
