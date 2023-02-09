from context import Context
from helpers import get_room_by_name
from .features import MOVABLE, USABLE
from .item import Item


class Parachute(Item):
    name = 'padak'
    description = 'Obyčajný padák MADE IN U.S.A. 1933'
    features = [MOVABLE, USABLE]

    def use(self, context: Context):
        # check usability
        # musim byt v miesntosti volny pad
        if context.current_room.name != 'voľný pád':
            print('Podľa teba som zrejme blbec, ale naozaj nechápem, na čo by to v tejto chvíli bolo dobré.')
            return

        # act
        # teleportujem sa do miestnosti pust
        context.current_room = get_room_by_name('púšť', context.world)

        # render
        print('Nad hlavou sa ti otvoril padák a po chvíli šťastne pristál...')
        context.current_room.show()
