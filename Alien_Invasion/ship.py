import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_setting, screen):

        super(Ship, self).__init__()

        self.screen = screen
        self.ai_settings = ai_setting

        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)
        self.bottom_y = float(self.rect.bottom)
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """update ship's position"""
        right_edge = self.ai_settings.screen_width-self.ai_settings.ship_size
        left_edge = self.ai_settings.ship_size
        up_edge = self.ai_settings.screen_height/2
        down_edge = self.ai_settings.screen_height

        if self.moving_right and self.center < right_edge:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.center > left_edge:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.bottom_y > up_edge:
            self.bottom_y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.bottom_y < down_edge:
            self.bottom_y += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center
        self.rect.bottom = self.bottom_y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.bottom_y = self.ai_settings.screen_height
