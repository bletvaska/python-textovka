from dataclasses import dataclass

from commands.command import Command
from context import Context


@dataclass
class LookAround(Command):
    name: str = 'rozhliadni sa'
    description: str = 'zobrazí opis miestnosti'

    def exec(self, context: Context, name):
        context.current_room.show()
