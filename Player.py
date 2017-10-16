import pygame
from resource_handler import *
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('player.png', -1)
        self.rect = self.rect.inflate(-20, -50)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.init_pos = pos
        self.rect.midleft = pos
        self.speed = speed
        self.alive = True
        self.on = True
        self.hp = 3
        pygame.time.set_timer(USEREVENT + 5, 500)
        self.firerate = 60
        self.fire = False
        self.image = pygame.transform.smoothscale(self.image,(100,40))

    def reinit(self, i):
        if i == 0:
            self.hp -= 1
            pygame.time.set_timer(USEREVENT + 1, 3000)
            pygame.time.set_timer(USEREVENT + 3, 300)
            pygame.time.set_timer(USEREVENT + 4, 100)
            self.alive = False
            self.rect.midleft = self.init_pos

    def move(self, x, y):
        newpos = self.rect.move((self.speed * x, self.speed * y))
        if self.area.contains(newpos):
            self.rect = newpos
