from context import Context
from utils import get_room_by_name


def _go(context: Context, direction: str):
    room = context.room

    # overim, ze ci sa na dany smer da ist
    # ak sa neda, tak vypisem spravu
    if direction not in room.exits or room.exits[direction] is None:
        print('Tam sa nedá ísť.')
        return

    # update history
    context.history.append(direction)

    # v opacnom pripade:
    # * zmenim aktualnu miestnost na novu
    context.room = get_room_by_name(room.exits[direction], context.world)

    # * rozhliadnem sa v nej
    context.room.show()
