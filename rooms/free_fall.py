from dataclasses import dataclass

from states import DEATH_BY_FREE_FALL
from .room import Room


@dataclass
class FreeFall(Room):
    def act(self, context):
        print('Stal si sa zakladateľom športového odvetvia, ktoré vojde do histórie ako skok hlboký.')
        context.game_state = DEATH_BY_FREE_FALL
