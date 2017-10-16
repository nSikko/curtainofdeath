import pygame
from resource_handler import *
from pygame.locals import *

class Boss2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('boss2.png', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.midright = (959,270)
        self.speed = 2
        self.hp = 30
        self.firerate = 34
        self.ofr = self.firerate
        self.ofrx = 2
        self.fr_duration = 125
        self.fr_init1 = self.fr_duration
        self.fr_init2 = 250
        self.fire = False
        self.firepattern = True
        self.score = 25000
        self.x = 0
        self.y = 1

    def update(self, x):
        self.hp -= x
        if self.hp > 0:
            self.move()
            self.shoot()

    def move(self):
        newpos = self.rect.move((self.speed * self.x, self.speed * self.y))
        self.rect = newpos
        if not self.area.collidepoint(self.rect.midtop) or not self.area.collidepoint(self.rect.midbottom):
            self.y = -(self.y)

    def shoot(self):
            if self.firerate == 0:
                self.fire = True
                if self.firepattern:
                    self.firerate = self.ofr
                else:
                    self.firerate = self.ofrx

            if self.fr_duration == 0:
                if self.firepattern:
                    self.firepattern = False
                    self.fr_duration = self.fr_init1
                else:
                    self.firepattern = True
                    self.fr_duration = self.fr_init2
            self.fr_duration -= 1
            self.firerate -= 1
