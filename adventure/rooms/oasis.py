from adventure import states
from adventure.helpers import get_item_by_type
from adventure.items.pharaos_necklace import PharaohsPlatinumNecklace
from adventure.rooms.room import Room


class Oasis(Room):
    def act(self, context):
        # check if indy has necklacke already
        necklace = get_item_by_type(PharaohsPlatinumNecklace, context.backpack)
        if necklace is None:
            return

        # render and set state
        print('Vidíš lietadlo, ktoré priletelo s tvojimi priateľmi z Káhiry.')
        context.game_state = states.WELL_DONE
