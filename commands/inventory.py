from dataclasses import dataclass

from .command import Command


@dataclass
class Inventory(Command):
    name: str = 'inventar'
    # aliases: list
    description: str = 'zobrazí obsah hráčovho batoha'

    def exec(self, room: dict, backpack: list):
        if len(backpack) == 0:
            print('Batoh je prázdny.')
        else:
            print('V batohu máš:')
            for item in backpack:
                print(f' * {item.name}')
