from dataclasses import dataclass
from typing import List

from items.item import Item
from .command import Command


@dataclass
class Inventory(Command):
    name: str = 'inventar'
    description: str = 'zobrazí obsah hráčovho batohu'

    def exec(self, context):
        if context.backpack == []:  # len(backpack) == 0:
            print('Batoh je prázdny.')
        else:
            print('V batohu máš:')
            for item in context.backpack:
                print(f'* {item.name}')
