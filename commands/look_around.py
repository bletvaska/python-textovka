# systemove importy/moduly
from dataclasses import dataclass

# tretostranove importy/moduly

# moje vlastne importy/moduly
from helper import show_room
from .command import Command


@dataclass
class LookAround(Command):
    name: str = 'rozhliadni sa'
    # aliases: list
    description: str = 'zobrazí opis miestnosti'

    def exec(self, room: dict, backpack: list):
        show_room(room)
