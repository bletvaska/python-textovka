from dataclasses import dataclass, field

from context import Context
from items.item import Item


@dataclass
class Inventory:
    name: str = 'inventar'
    description: str = 'zobrazí obsah hráčovho batohu'
    aliases: list[str] = field(default_factory=lambda: ['inventory', 'i'])

    def exec(self, line, context: Context):
        if len(context.backpack) == 0:
            print('Batoh je prázdny.')
        else:
            print('V batohu máš:')
            for item in context.backpack:
                print(f'* {item.name}')
