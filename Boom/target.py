'''
    contains the 'target' sprite and its features
'''

import pygame
from Boom.constants import TARGET_SIZE
from Boom.constants import SELF_DESTRUCTION
from Boom.signs import Sign


class Target(pygame.sprite.Sprite):
    def __init__(self, pos, spawn_time, score, sign_group) -> None:
        super().__init__()

        self.sign_event = pygame.event.Event(pygame.USEREVENT + 3)
        target_surface = pygame.image.load(
            'assets/khamenei.png').convert_alpha()
        target = pygame.transform.scale(target_surface, TARGET_SIZE)

        self.pos = pos
        self.image = target
        self.rect = target.get_rect(center=self.pos)
        self.spawn_time = spawn_time
        self.score = score
        self.sign_group = sign_group

        self.kill_sound = pygame.mixer.Sound('assets/kill_sound.mp3')

    # target gets destroyed after clicking on it.
    # meaning: detecting collision with the target sprtie
    def destroy(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicks = pygame.mouse.get_pressed()
        if self.rect.collidepoint(mouse_pos) and mouse_clicks[0]:
            self.sign_group.add(
                Sign(pygame.time.get_ticks(), self.get_pos(), 'one'))
            self.score.increase()
            self.kill_sound.play()
            self.kill()

    def get_pos(self):
        return self.pos

    # self destruction after a said time
    def self_destruct(self):
        if (pygame.time.get_ticks() - self.spawn_time) > SELF_DESTRUCTION:
            self.sign_group.add(
                Sign(pygame.time.get_ticks(), self.get_pos(), 'two'))
            self.score.decrease()
            self.kill()

    def update(self):
        self.destroy()
        self.self_destruct()
