import states
from .room import Room


class Oasis(Room):

    def act(self, context):
        print('Dosiahol si cieľ svojej cesty.')
        context.game_state = states.STATE_VICTORY
