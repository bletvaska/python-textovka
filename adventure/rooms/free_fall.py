import states
from context import Context
from .room import Room


class FreeFall(Room):
    steps = 1

    def act(self, context: Context):
        # decrease nr of steps
        if self.steps != 0:
            self.steps = self.steps - 1
            return

        # death of indiana jones
        print('Stal si sa zakladateľom športového odvetvia, ktoré vojde do histórie ako skok hlboký.')

        context.game_state = states.DEATH_BY_FREE_FALL
