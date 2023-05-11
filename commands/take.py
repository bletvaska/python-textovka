from rich import print

from helpers import get_item_by_name
from items.features import MOVABLE
from .command import Command


class Take(Command):
    name = 'vezmi'
    description = 'vloží do batohu zvolený predmet'

    def exec(self, context):
        # when no param was given
        # len(self.param) == 0
        if self.param == '':
            print('Neviem, aký predmet chceš vziať.')
            return

        # search for item in backpack
        item = get_item_by_name(self.param, context.current_room.items)

        # was item found in backpack?
        if item == None:
            print('Taký predmet tu nikde nevidím.')
            return

        # is item movable?
        if MOVABLE not in item.features:
            print('Tento predmet sa nedá vziať.')
            return

        # is backpack full?
        if len(context.backpack) >= 1:
            print('Batoh je plný.')
            return

        # take item from current room
        context.current_room.items.remove(item)
        context.backpack.append(item)

        # render
        print(f'Do batohu si si vložil predmet [magenta bold]{item.name}[/magenta bold].')
