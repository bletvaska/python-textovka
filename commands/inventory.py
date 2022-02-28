from dataclasses import dataclass, field
from typing import List

from context import Context
from .command import Command


@dataclass
class Inventory(Command):
    name: str = 'inventar'
    # aliases: List[str] = field(default_factory=['inventory', 'i'])
    description: str = 'zobrazí obsah hráčovho batoha'

    def exec(self, context: Context, param: str):
        if len(context.backpack) == 0:
            print('Batoh je prázdny.')
            return

        print('V batohu máš:')
        for item in context.backpack:
            print(f' * {item.name}')
