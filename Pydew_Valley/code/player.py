import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __int__(self, pos, group):
        super().__init__(group)

        # What the sprite will look like.
        self.image = pygame.Surface((32, 64))
        self.image.fill('blue')
        self.rect = self.image.get_rect(center=pos)
