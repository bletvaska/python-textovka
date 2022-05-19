from dataclasses import dataclass

from commands.command import Command
from context import Context


@dataclass
class LookAround(Command):
    name: str = 'rozhliadni sa'
    description: str = 'vypíše opis aktuálnej miestnosti'

    def exec(self, context: Context):
        context.current_room.show()
