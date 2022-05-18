from dataclasses import dataclass

from context import Context
from room import Room


@dataclass
class LookAround:
    name: str = 'rozhliadni sa'
    description: str = 'vypíše opis aktuálnej miestnosti'

    def exec(self, line, context: Context):
        context.current_room.show()
