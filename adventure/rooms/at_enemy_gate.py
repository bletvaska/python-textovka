import states
from rooms import Room
from rooms.directions import SOUTH


class AtEnemyGate(Room):
    def act(self, context):
        for item in context.backpack:
            if item.name == 'nemecka uniforma (oblecena)':
                if SOUTH not in context.current_room.exits:
                    context.current_room.exits[SOUTH] = 'v tábore'
                    context.score += 5
                    print('Keď ťa vojak uvidel, otvoril ti bránu (hlupák).')
                return
        else:
            print('Vojak si ťa so záujmom prehliadol a zastrelil ťa...')
            context.game_state = states.SHOT_BY_ENEMY
