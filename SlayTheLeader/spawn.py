from SlayTheLeader.constants import TARGET_SPAWN
from random import choice


# a spawn algorithms which will spawn the targets
# randomally in the 4x4 grid each time.
# no target will be spawned in a currently
# occupied tile
def spawn_target(target_group):
    while len(target_group) < 12:
        switch = True
        pos = choice(TARGET_SPAWN)
        for target in target_group:
            if pos == target.get_pos():
                switch = False
                break
        if switch:
            return pos
    return (0, 0)
