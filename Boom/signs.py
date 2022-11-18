'''
    a sprite for 'signs' with its features which consists of 
    two signs : Green number one, Red number two
'''

import pygame
from Boom.constants import SIGN_SIZE, SIGN_SELF_DESTRUCTION


class Sign(pygame.sprite.Sprite):
    def __init__(self, spawn_time, pos, type):
        super().__init__()

        self.pos = pos
        self.spawn_time = spawn_time
        one_pic = pygame.image.load('assets/one.png')
        one = pygame.transform.scale(one_pic, SIGN_SIZE)
        two_pic = pygame.image.load('assets/two.png')
        two = pygame.transform.scale(two_pic, SIGN_SIZE)
        if type == 'one':
            self.image = one
            self.rect = one.get_rect(center=pos)
        elif type == 'two':
            self.image = two
            self.rect = two.get_rect(center=pos)

    # self destruction after a said time
    def self_destruct(self):
        if (pygame.time.get_ticks() - self.spawn_time) > SIGN_SELF_DESTRUCTION:
            self.kill()

    def update(self):
        self.self_destruct()
