# systemove importy/moduly
from dataclasses import dataclass, field

# tretostranove importy/moduly

# moje vlastne importy/moduly
from typing import List

from context import Context
from helper import show_room
from .command import Command


@dataclass
class LookAround(Command):
    name: str = 'rozhliadni sa'
    # aliases: List[str] = field(default_factory=['look around'])
    description: str = 'zobrazí opis miestnosti'

    def exec(self, context: Context):
        show_room(context.room)
