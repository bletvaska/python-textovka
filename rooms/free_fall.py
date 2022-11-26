from dataclasses import dataclass

from states import DEATH_BY_FREE_FALL
from .room import Room


@dataclass
class FreeFall(Room):
    steps: int = 0

    def act(self, context):
        self.steps += 1

        # too many steps?
        if self.steps > 1:
            print('Stal si sa zakladateľom športového odvetvia, ktoré vojde do histórie ako skok hlboký.')
            context.game_state = DEATH_BY_FREE_FALL
