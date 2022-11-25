from dataclasses import dataclass

from helpers import get_item_by_name
from states import SHOT_BY_ENEMY, DEATH_BY_FREE_FALL
from .room import Room


@dataclass
class FreeFall(Room):
    def on_enter(self, context):
        print('Ta si spadol a zabil sa bez padaka.')
        context.game_state = DEATH_BY_FREE_FALL
