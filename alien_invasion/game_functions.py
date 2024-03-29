import sys
import pygame
import json
from time import sleep

from bullet import Bullet
from alien import Alien

def fire_bullet(bullets, ai_settings, screen, ship, gs):
    """如果还没有达到限制， 就发射一颗子弹"""
    #创建一颗子弹，并将其加入到编组Bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        gs.shooting_sound()

def check_key_down_events(event, ai_settings, screen, ship, bullets, stats,
        aliens, sb, gs):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if stats.game_active:
            fire_bullet(bullets, ai_settings, screen, ship, gs)
    elif event.key == pygame.K_q:
        game_exit(stats)
    elif event.key == pygame.K_p:
        if not stats.game_active:
            start_game(stats, aliens, bullets, ship, screen, ai_settings, sb)

def check_key_up_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, play_button, ship, aliens,
        bullets, sb, fb, gs):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit(stats)
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ai_settings, screen, ship, bullets,
                stats, aliens, sb, gs)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship,
                aliens, bullets, mouse_x, mouse_y, sb)
        elif event.type == fb.COUNT:
            fb.update_fps()

def check_play_button(ai_settings, screen, stats, play_button, ship, aliens,
        bullets, mouse_x, mouse_y, sb):
    """在玩家单机Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(stats, aliens, bullets, ship, screen, ai_settings, sb)

def start_game(stats, aliens, bullets, ship, screen, ai_settings, sb):
    #重置游戏设置
    ai_settings.initialize_dynamic_settings()

    #隐藏光标
    pygame.mouse.set_visible(False)

    #重置游戏统计信息
    stats.reset_stats()
    stats.game_active = True

    #重置记分牌图像
    sb.prep_image()

    #清空外星人列表和子弹列表
    aliens.empty()
    bullets.empty()

    #创建一群外星人， 并让飞船居中
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
        play_button, fb):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)

    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.drew_bullet()
    ship.blitme()
    aliens.draw(screen)

    #显示得分
    sb.show_score()

    #显示帧数
    fb.show_fps()

    #游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    #让最近绘制的屏幕可见
    pygame.display.flip()

    #更新帧数
    fb.frames += 1

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, gs):
    bullets.update()

    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens,
            bullets, gs)

def check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens,
        bullets, gs):
    """响应子弹和外星人的碰撞"""
    #删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)

    if collisions:
        for collided_aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(collided_aliens)
            sb.prep_score()
        check_high_score(stats, sb)
        gs.explosive_sound()

    if len(aliens) == 0:
        start_new_level(bullets, ai_settings, stats, sb, screen, ship, aliens)

def start_new_level(bullets, ai_settings, stats, sb, screen, ship, aliens):
    #如果整群外星人都被消灭， 就提高一个等级
    bullets.empty()
    ai_settings.increase_speed()

    #提高等级
    stats.level += 1
    sb.prep_level()

    create_fleet(ai_settings, screen, ship, aliens)



def get_number_alien_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height -
        3 * alien_height - ship_height)
    number_rows = int(available_space_y/(2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_number * alien_width
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    #创建一个外星人，并计算一行可容纳多少个外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_alien_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)
    #创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edge(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """将整群外星人向下移， 并改变他们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, aliens, bullets, screen, ship, sb):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        #将ships_left减1
        stats.ships_left -= 1

        #更新记分牌
        sb.prep_ship()

        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新的外星人，并将飞船放到屏幕底部中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def update_aliens(ai_settings, ship, aliens, stats, bullets, screen, sb):
    """
    检查是否有外星人位于屏幕边缘，并更新整群外星人的位置
    """
    check_fleet_edge(ai_settings, aliens)
    aliens.update()

    #检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, aliens, bullets, screen, ship, sb)

    #检查是否有外星人抵达屏幕底部
    check_alien_bottom(ai_settings, stats, aliens, bullets, screen, ship, sb)

def check_alien_bottom(ai_settings, stats, aliens, bullets, screen, ship, sb):
    """是否有外星人到达屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #像飞船被外星人撞到一样处理
            ship_hit(ai_settings, stats, aliens, bullets, screen, ship, sb)
            break

def check_high_score(stats, sb):
    """检查是否产生了新的最高得分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def game_exit(stats):
    with open('high_score.json', 'w') as f_obj:
        json.dump(stats.high_score, f_obj)
    sys.exit()
