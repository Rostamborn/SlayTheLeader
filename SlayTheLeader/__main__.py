import pygame
from sys import exit
from SlayTheLeader.controller import ProgramController
from SlayTheLeader.constants import FPS, SPAWN_TIME
from SlayTheLeader.target import Target
from SlayTheLeader.spawn import spawn_target
from SlayTheLeader.score_manager import ScoreManager
from SlayTheLeader.constants import SCREEN_SIZE
from SlayTheLeader.timer_sprite import GameTimer


def main_loop() -> None:
    target_spawn = SPAWN_TIME
    while True:
        # a list of target sprites
        target_group = controller.get_target_group().sprites()

        # handling events in the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Handling Spawn based on the custom event timer
            if event.type == target_spawn_timer:
                valid_pos = spawn_target(target_group)
                if valid_pos != (0, 0):
                    controller.add_target(
                        Target(valid_pos, pygame.time.get_ticks(), score, sign_group))

            # Event for the 60 second timer
            if event.type == count_down and controller.get_state() == 'game':
                game_timer.tick()

                # increasing the spawn speed each second by reducing the delay
                # for target_spawn_timer
                pygame.time.set_timer(target_spawn_timer, target_spawn)
                if target_spawn > 300:
                    target_spawn -= 50

        # Reset spawn time after gameover
        if controller.get_state() == 'gameover':
            target_spawn = SPAWN_TIME

        controller.run()
        clock.tick(FPS)
        pygame.display.update()


if __name__ == '__main__':
    # Initializing basic stuff for the program
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    score = ScoreManager()
    game_timer = GameTimer()
    sign_group = pygame.sprite.Group()
    controller = ProgramController(screen, game_timer, sign_group, score)
    pygame.display.set_caption('Boom')
    target_spawn_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(target_spawn_timer, SPAWN_TIME)
    count_down = pygame.USEREVENT + 2
    pygame.time.set_timer(count_down, 1000)
    clock = pygame.time.Clock()
    main_loop()
