import pygame
from resource_handler import *
from pygame.locals import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, speed, enemy):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('bullet.png', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.center = pos
        self.onscreen = True
        self.speed = speed
        self.firerate = 60
        if enemy:
            self.image = pygame.transform.flip(self.image, 1, 0)

    def update(self):
        self.move()

    def move(self):
        newpos = self.rect.move(-(self.speed), 0)
        self.rect = newpos
        if not self.area.collidepoint(self.rect.midright):
            self.onscreen = False
