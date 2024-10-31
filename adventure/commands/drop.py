from rich import print

from helpers import get_item_by_name
from .command import Command


class Drop(Command):
    name: str = 'poloz'
    description: str = 'vyberie zvolený predmet z batohu a položí ho do aktuálnej miestnosti'

    def exec(self, context, param):
        if param == '':
            print('Neviem čo chceš položiť.')
            return

        item = get_item_by_name(param, context.backpack)
        if item is None:
            print('Taký predmet pri sebe nemáš.')
            return

        # action
        context.backpack.remove(item)
        context.current_room.items.append(item)
        print(f'Do miestnosti si položil [bold magenta]{item.name}[/bold magenta].')

        context.history.append(f'{self.name} {param}')
