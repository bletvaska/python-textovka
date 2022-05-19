from dataclasses import dataclass

from context import Context


@dataclass
class LookAround:
    name: str = 'rozhliadni sa'
    description: str = 'vypíše opis aktuálnej miestnosti'

    def exec(self, context: Context):
        context.current_room.show()
