from dataclasses import dataclass

from context import Context
from .command import Command


@dataclass
class Inventory(Command):
    name: str = 'inventar'
    description: str = 'zobrazí obsah hráčovho batohu'

    def exec(self, context: Context, arg: str):
        backpack = context.backpack['items']

        if backpack == []:
            print('Batoh je prázdny.')
        else:
            print("V batohu máš:")
            for item in backpack:
                print(f'\t* {item.name}')
