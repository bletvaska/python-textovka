from .features import MOVABLE, USABLE
from .item import Item


class Parachute(Item):
    name = 'padak'
    description = 'Made in USA 1939'
    features = [MOVABLE, USABLE]

    def use(self, context):
        # check if it is possible to use parachute here
        # if not in correct room, then

        # if context.current_room.name != FreeFall.name:
        if context.current_room.name != 'voľný pád':
            print('Podľa teba som zrejme blbec, ale naozaj nechápem, k čomu by to v súčasnej dobe bolo dobré.')
            return

        # action

        # render
        print('pouzivam padak')
