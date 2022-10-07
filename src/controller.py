'''
    controls the program flow
'''
import pygame
from Boom.src.target import Target
from Boom.src.constants import SCREEN_SIZE


class ProgramController():
    def __init__(self, screen, gametimer, sign_group, score=None) -> None:
        self.screen = screen
        self.state = 'menu'
        self.score = score

        # Font
        self.font = pygame.font.Font(None, 40)

        # Surfaces and Rects
        self.message_su = self.font.render(
            "press SPACE to play", False, 'Black')
        self.message_rect = self.message_su.get_rect(
            center=(SCREEN_SIZE[0]//2, 425))

        game_background_pic = pygame.image.load('Boom/assets/background.jpg')
        self.game_background = pygame.transform.scale(
            game_background_pic, (500, 700))

        gameover_background_pic = pygame.image.load(
            'Boom/assets/gameover_background.jpg')
        self.gameover_background = pygame.transform.scale(
            gameover_background_pic, SCREEN_SIZE)

        status_bar_pic = pygame.image.load('Boom/assets/status_bar.jpg')
        self.status_bar = pygame.transform.scale(status_bar_pic, (500, 50))

        # Groups
        self.target_group = pygame.sprite.Group()
        self.game_timer = pygame.sprite.GroupSingle()
        self.game_timer.add(gametimer)
        self.sign_group = sign_group

    # Check for current state
    def run(self) -> None:
        if self.state == 'game':
            self.run_game()
        elif self.state == 'menu':
            self.run_menu()
        elif self.state == 'gameover':
            self.run_gameover()

    def set_state(self, state) -> None:
        self.sign_group.empty()
        self.target_group.empty()
        self.state = state

    def get_state(self) -> str:
        return self.state

    # main game meterial in the main loop
    def run_game(self) -> None:
        self.screen.blit(self.game_background, (0, 0))
        self.screen.blit(self.status_bar, (0, 700))
        self.target_group.draw(self.screen)
        self.target_group.update()
        self.game_timer.draw(self.screen)
        self.game_timer.update()
        self.sign_group.draw(self.screen)
        self.sign_group.update()

        if self.score is not None:
            self.score.set_pos((10, 710))
            self.score.show()
            if self.score.get_score() < 0 or self.game_timer.sprite.get_time() <= 0:
                self.set_state('gameover')
                self.game_timer.sprite.set_time(60)

    # menu material in the main loop
    def run_menu(self) -> None:
        keys = pygame.key.get_pressed()
        self.screen.blit(self.gameover_background, (0, 0))
        self.screen.blit(self.message_su, self.message_rect)
        if keys[pygame.K_SPACE]:
            self.set_state("game")
            self.score.set_zero()

    # gameover surface material in the main loop
    def run_gameover(self) -> None:
        keys = pygame.key.get_pressed()
        self.screen.blit(self.gameover_background, (0, 0))
        self.screen.blit(self.message_su, self.message_rect)

        if self.score is not None:
            self.score.set_pos((140, 300))
            self.score.show()

        if keys[pygame.K_SPACE]:
            self.set_state("game")
            self.score.set_zero()

    # Add target to the target Group
    def add_target(self, target: Target) -> None:
        self.target_group.add(target)

    def get_target_group(self) -> None:
        return self.target_group
