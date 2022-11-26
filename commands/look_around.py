from dataclasses import dataclass

from helpers import get_current_room
from .command import Command


@dataclass
class LookAround(Command):
    name: str = 'rozhliadni sa'
    description: str = 'rozhliadne sa v aktuálnej miestnosti'

    def exec(self, context):
        room = get_current_room(context)
        room.show()
