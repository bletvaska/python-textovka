from dataclasses import dataclass

from .command import Command


@dataclass
class Inventory(Command):
    # fields
    name: str = 'inventar'
    description: str = 'zobrazí obsah hráčovho batohu'

    # methods
    def exec(self, context, param):
        if len(context.backpack) == 0:
            print('Batoh je prázdny.')
        else:
            print('V batohu máš:')
            for item in context.backpack:
                print(f'* {item}')
