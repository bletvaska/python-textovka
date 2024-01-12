from rich import print

from helpers import get_item_by_name
from .command import Command


class Drop(Command):
    name: str = 'poloz'
    description: str = 'vyberie zvolený predmet z batohu a položí ho do aktuálnej miestnosti'

    def exec(self, context):
        # if no item was entered
        if self.param == '':
            print("Neviem, čo chceš položiť.")
            return

        # search for item in room
        item = get_item_by_name(self.param, context.backpack)

        # was item found?
        if item is None:
            print('Taký predmet pri sebe nemáš.')
            return

        # drop item
        context.backpack.remove(item)
        context.current_room.items.append(item)
        item.on_drop(context)

        # render
        print(f'Do miestnosti si položil [bold magenta]{item.name}[/bold magenta].')

        # append command to history
        context.history.append(f'{self.name} {self.param}')
