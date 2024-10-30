from rich import print

from helpers import get_item_by_name
from items.features import MOVABLE
from .command import Command


class Take(Command):
    name: str = 'vezmi'
    description: str = 'vezme predmet z aktuálnej miestnosti a vloží ho do batohu'

    def exec(self, context, param):
        if param == '':
            print('Neviem, čo chceš zobrať.')
            return

        item = get_item_by_name(param, context.current_room.items)
        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        if MOVABLE not in item.features:
            print('Tento predmet sa nedá zobrať.')
            return

        # action
        context.current_room.items.remove(item)
        context.backpack.append(item)
        print(f'Do batohu si vložil predmet [bold magenta]{item.name}[/bold magenta].')
