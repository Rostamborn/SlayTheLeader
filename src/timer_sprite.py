'''
    contains the 'Timer' sprite and its features
    which will be shown in the game as a 60 secons timer
'''

import pygame


class GameTimer(pygame.sprite.Sprite):
    def __init__(self, time=60) -> None:
        super().__init__()

        self.time = time
        self.font = pygame.font.Font(None, 60)
        self.image = self.font.render(f"Time: {self.time}", False, 'Black')
        self.rect = self.image.get_rect(topleft=(320, 710))

    def tick(self):
        self.time -= 1
        self.image = self.font.render(f"Time: {self.time}", False, 'Black')

    def set_time(self, time):
        self.time = time
        self.image = self.font.render(f"Time: {self.time}", False, 'Black')

    def get_time(self):
        return self.time
