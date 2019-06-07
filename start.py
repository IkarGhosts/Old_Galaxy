import sys


import pygame
from pygame.sprite import Group


from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats


import game_func as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Old Galaxy")
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens, ship)

    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets, aliens, ai_settings, screen, ship)
        gf.update_aliens(ai_settings, aliens, ship, stats, screen, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
