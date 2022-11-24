from dataclasses import dataclass

from directions import DOWN
from helpers import get_room_by_name
from .command import Command


@dataclass
class Down(Command):
    name: str = 'dolu'
    description: str = 'presunie sa do miestnosti dolu od aktuálnej'

    def exec(self, context):
        room = get_room_by_name(context.current_room, context.rooms)
        if DOWN in room.exits:
            print('idem dolu')
        else:
            print('Tam sa nedá ísť.')
