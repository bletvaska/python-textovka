from rich import print

from helpers import get_item_by_name
from items.features import MOVABLE
from .command import Command


class Take(Command):
    name: str = 'vezmi'
    description: str = 'vezme predmet z miestnosti a vloží ho do batohu'

    def exec(self, context):
        item_name = self.param

        # if not item was entered
        if item_name == '':
            print('Neviem, čo chceš zobrať.')
            return

        # if not in room
        item = get_item_by_name(item_name, context.current_room.items)
        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        if MOVABLE not in item.features:
            print('Tento predmet sa nedá zobrať.')
            return

        if len(context.backpack) >= 5:
            print('Batoh je plný.')
            return

        context.backpack.append(item)
        context.current_room.items.remove(item)
        print(f'Do batohu si vložil predmet [bold magenta]{self.param}[/bold magenta].')

