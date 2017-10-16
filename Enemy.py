import pygame
from resource_handler import *
from pygame.locals import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, posx, posy, speed, image, hp, firerate, x, y, pattern, prate, score):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(image, -1)
        screen = pygame.display.get_surface()
        self.name = image
        self.area = screen.get_rect()
        self.rect.midright = (posx,posy)
        self.speed = speed
        self.hp = hp
        self.pattern = pattern
        self.prate = prate
        self.opr = prate
        self.change = True
        self.firerate = firerate
        self.ofr = firerate
        self.fire = False
        self.score = score
        self.x = x
        self.y = y

    def update(self, x):
        self.hp -= x
        if self.hp > 0:
            self.move()
            self.shoot()
            self.direction()

    def move(self):
        newpos = self.rect.move((self.speed * self.x, self.speed * self.y))
        self.rect = newpos
        if not self.area.collidepoint(self.rect.midright):
            self.hp = -1

    def shoot(self):
        if self.firerate != -1:
            if self.firerate == 0:
                self.fire = True
                self.firerate = self.ofr
            self.firerate -= 1

    def direction(self):
        # standard
        if self.pattern > 0:
            if self.prate == 0:
                # zig zag (up first) if x == 0 vertical only
                if self.pattern == 1:
                    if self.change:
                        self.y = -1
                    else:
                        self.y = 1
                # zig zag (reverse) if x == 0 vertical only
                elif self.pattern == 2:
                    if not self.change:
                        self.y = -1
                    else:
                        self.y = 1
                # single up
                elif self.pattern == 3:
                    if self.change:
                        self.y = -1
                    else:
                        self.y = 0
                # single down
                elif self.pattern == 4:
                    if self.change:
                        self.y = 1
                    else:
                        self.y = 0
                self.prate = self.opr
                self.change = not self.change
            else:
                self.prate -= 1
