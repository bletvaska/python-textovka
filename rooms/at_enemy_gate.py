from dataclasses import dataclass

from helpers import get_item_by_name
from states import SHOT_BY_ENEMY
from .room import Room


@dataclass
class AtEnemyGate(Room):
    def on_enter(self, context):
        uniform = get_item_by_name('nemecka uniforma (oblecena)', context.backpack)

        # is indy wearing a uniform?
        if uniform is None:
            print('Vojak si ťa so záujmom prehliadol a zastrelil ťa.')
            context.game_state = SHOT_BY_ENEMY
        else:
            print('Keď ťa vojak uvidel, otvoril ti bránu. (Hlupák!)')
