from dataclasses import dataclass

from helpers import get_item_by_name
from states import SHOT_BY_ENEMY
from . import directions
from .room import Room


@dataclass
class AtEnemyGate(Room):
    def act(self, context):
        uniform = get_item_by_name('nemecka uniforma (oblecena)', context.backpack)

        # is indy wearing a uniform?
        if uniform is None:
            # action
            context.game_state = SHOT_BY_ENEMY

            # render
            print('Vojak si ťa so záujmom prehliadol a zastrelil ťa.')
        else:
            # action
            context.current_room.exits[directions.SOUTH] = 'v tábore'

            # render
            print('Keď ťa vojak uvidel, otvoril ti bránu. (Hlupák!)')
