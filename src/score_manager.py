'''
    a class that manages the score system of the game
'''
import pygame
from Boom.src.constants import SCORE_INCREASE, SCORE_DECREASE


class ScoreManager():
    def __init__(self, x: int = 10, y: int = 710) -> None:
        self.score = 0
        self.screen = pygame.display.get_surface()
        self.x, self.y = x, y
        self.font = pygame.font.Font(None, 60)

    def increase(self) -> None:
        self.score += SCORE_INCREASE

    def decrease(self) -> None:
        self.score -= SCORE_DECREASE

    def set_pos(self, pos) -> None:
        self.x, self.y = pos[0], pos[1]

    def set_zero(self) -> None:
        self.score = 0

    def get_score(self) -> int:
        return self.score

    def show(self) -> None:
        score_su = self.font.render(
            f"SCORE: {str(self.score)}", False, 'Black')
        score_rect = score_su.get_rect(topleft=(self.x, self.y))
        self.screen.blit(score_su, score_rect)
