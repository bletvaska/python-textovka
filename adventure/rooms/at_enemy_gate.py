from helpers import get_item_by_name
import states
from . import directions
from .room import Room


class AtEnemyGate(Room):
    def act(self, context):
        uniform = get_item_by_name('nemecku uniformu', context.backpack)

        # is indy wearing a uniform?
        if uniform is None or uniform.is_dressed is False:
            # action
            context.game_state = states.SHOT_BY_ENEMY

            # render
            print('Vojak si ťa so záujmom prehliadol a zastrelil ťa.')

        elif directions.SOUTH not in context.current_room.exits:
            # action
            context.current_room.exits[directions.SOUTH] = 'v tábore'

            # render
            print('Keď ťa vojak uvidel, otvoril ti bránu. (Hlupák!)')
