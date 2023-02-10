from rich import print

from helpers import get_item_by_name
from items.features import MOVABLE
from .command import Command


class Take(Command):
    name = 'vezmi'
    description = 'vezme predmet z miestnosti a vloží ho do batohu'

    def exec(self, context):
        # if no item was entered
        if self.param == '':
            print("Neviem, čo chceš zobrať.")
            return

        # search for item in room
        item = get_item_by_name(self.param, context.current_room.items)

        # was item found?
        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        # is item movable?
        if MOVABLE not in item.features:
            print('Tento predmet sa nedá zobrať.')
            return

        # take item
        context.current_room.items.remove(item)
        context.backpack.append(item)

        # render
        print(f'Do batohu si si vložil [bold magenta]{item.name}[/bold magenta].')

        # append command to history
        context.history.append(f'{self.name} {self.param}')
