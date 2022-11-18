'''
    A list of all the constatns that will be used and
    accessed throughout the program
'''

SCREEN_SIZE = (600, 750)
STATUSBAR_SIZE = (SCREEN_SIZE[0], SCREEN_SIZE[1]//15)
FPS = 60
GAME_NAME = 'Boom'
TARGET_SIZE = (100, 130)
SIGN_SIZE = (110, 160)
SELF_DESTRUCTION = 2000
SIGN_SELF_DESTRUCTION = 300
SPAWN_TIME = 1000
SCORE_INCREASE, SCORE_DECREASE = 1, 2

xCo, yCo = SCREEN_SIZE[0]//8, (SCREEN_SIZE[1]-STATUSBAR_SIZE[1])//8

TARGET_SPAWN = (
    (xCo, 87), (3*xCo, 87), (5*xCo, 87), (7*xCo, 87),
    (xCo, 262), (3*xCo, 262), (5*xCo, 262), (7*xCo, 262),
    (xCo, 437), (3*xCo, 437), (5*xCo, 437), (7*xCo, 437),
    (xCo, 612), (3*xCo, 612), (5*xCo, 612), (7*xCo, 612)
)
