import sys


import pygame

from settings import Settings
from ship import Ship

import game_func as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_heigth)
    )
    pygame.display.set_caption("Old Galaxy")
    ship = Ship(ai_settings, screen)

    while True:

        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
