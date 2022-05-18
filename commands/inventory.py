from dataclasses import dataclass, field

from items.item import Item


@dataclass
class Inventory:
    name: str = 'inventar'
    description: str = 'zobrazí obsah hráčovho batohu'
    aliases: list[str] = field(default_factory=lambda: ['inventory', 'i'])

    def exec(self, backpack: list[Item]):
        if len(backpack) == 0:
            print('Batoh je prázdny.')
        else:
            print('V batohu máš:')
            for item in backpack:
                print(f'* {item.name}')
