from rich import print

from helpers import get_item_by_name
from .command import Command


class Drop(Command):
    name: str = 'poloz'
    description: str = 'vyberie zvolený predmet z batohu a položí ho do aktuálnej miestnosti'

    def exec(self, context):
        item_name = self.param

        if item_name == '':
            print('Neviem čo chceš položiť.')
            return

        item = get_item_by_name(item_name, context.backpack)
        if item is None:
            print('Taký predmet pri sebe nemáš.')
            return

        context.history.append(f'{self.name} {item_name}')

        context.backpack.remove(item)
        context.current_room.items.append(item)
        print(f'Do miestnosti si položil predmet [bold magenta]{item.name}[/bold magenta].')
