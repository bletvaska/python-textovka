from adventure import states
from .room import Room


class FreeFall(Room):
    steps: int = 2

    def act(self, context):
        self.steps -= 1

        # too many steps?
        if self.steps == 0:
            print('Stal si sa zakladateľom športového odvetvia, ktoré vojde do histórie ako skok hlboký.')
            context.game_state = states.DEATH_BY_FREE_FALL
