import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the play button
    play_button = Button(ai_settings, screen, "Play")
    # Create an instance to store game statistics and scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # make a ship
    ship = Ship(ai_settings, screen)
    # make a group to store bullets in, make alien group, stars group
    bullets = Group()
    aliens = Group()
    stars = Group()
    gf.create_stars(ai_settings, screen, stars)
    # create alien fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets, aliens, sb)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, aliens, ship, bullets, sb)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         stars, play_button)


if __name__ == "__main__":
    run_game()
