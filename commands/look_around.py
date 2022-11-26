from dataclasses import dataclass

from .command import Command


@dataclass
class LookAround(Command):
    name: str = 'rozhliadni sa'
    description: str = 'rozhliadne sa v aktuálnej miestnosti'

    def exec(self, context):
        context.current_room.show()
