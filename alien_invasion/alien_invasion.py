import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_functions as gf
from button import Button
from scoreboard import Scoreboard
from fps import Fps
from game_sounds import GameSounds

def run_game():
    #初始化游戏、设置和屏幕对象
    pygame.init()
    pygame.mixer.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 声音实例
    gs = GameSounds()

    #创建Play按钮
    play_button = Button(ai_settings, screen, 'Play')

    #创建一个用于存储游戏统计信息的实例，并创建积分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #创建fps模块实例
    fb = Fps(screen)

    #创建一艘飞船，一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens,
            bullets, sb, fb, gs)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                bullets, gs)
            gf.update_aliens(ai_settings, ship, aliens, stats, bullets, screen,
                sb)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
            play_button, fb)



run_game()
