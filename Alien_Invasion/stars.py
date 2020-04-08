import pygame
from pygame.sprite import Sprite


class Star(Sprite):

    def __init__(self, ai_settings, screen, random_star):
        super(Star, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load image
        self.image1 = pygame.image.load('image/star.bmp')
        self.image2 = pygame.image.load('image/star2.bmp')
        self.image3 = pygame.image.load('image/star3.bmp')
        self.rect = self.image1.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        if random_star == 0:
            self.image = self.image1
        elif random_star == 1:
            self.image = self.image2
        else:
            self.image = self.image3

    def blitme(self):
        self.screen.blit(self.image, self.rect)

