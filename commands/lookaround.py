from dataclasses import dataclass

from room import Room


@dataclass
class LookAround:
    name: str = 'rozhliadni sa'
    description: str = 'vypíše opis aktuálnej miestnosti'

    def exec(self, room: Room):
        room.show()
