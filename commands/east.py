from dataclasses import dataclass

from rooms import directions
from helpers import get_current_room
from .command import Command


@dataclass
class East(Command):
    name: str = 'vychod'
    description: str = 'presunie sa do miestnosti na východ od aktuálnej'

    def exec(self, context):
        # get current room by its name
        room = get_current_room(context)

        # is there exit going down?
        if directions.EAST in room.exits:
            context.current_room = room.exits[directions.EAST]
            room = get_current_room(context)
            room.show()

        else:
            print('Tam sa nedá ísť.')
