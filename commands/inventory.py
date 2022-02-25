from dataclasses import dataclass, field
from typing import List

from .command import Command


@dataclass
class Inventory(Command):
    name: str = 'inventar'
    # aliases: List[str] = field(default_factory=['inventory', 'i'])
    description: str = 'zobrazí obsah hráčovho batoha'

    def exec(self, room: dict, backpack: list):
        if len(backpack) == 0:
            print('Batoh je prázdny.')
        else:
            print('V batohu máš:')
            for item in backpack:
                print(f' * {item.name}')
