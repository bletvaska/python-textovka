from dataclasses import dataclass

from .command import Command


@dataclass
class LookAround(Command):
    name: str = 'rozhliadni sa'
    description: str = 'rozhliadne sa v aktuálnej miestnosti'

    def exec(self, context):
        room = get_room_by_name(context.current_room, context.rooms)
        print(room.description)
