from dataclasses import dataclass

from .command import Command


@dataclass
class Inventory(Command):
    name: str = 'inventar'
    description: str = 'zobrazí obsah batohu'

    def exec(self, context):
        if len(context.backpack) == 0:  # backpack == []
            print('Batoh je prázdny.')
        else:
            print('V batohu máš:')
            for item in context.backpack:
                print(f'* {item.name}')
