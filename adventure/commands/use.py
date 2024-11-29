from rich import print

from helpers import get_item_by_name
from items.features import USABLE
from .command import Command


class Use(Command):
    name: str = 'pouzi'
    description: str = 'použije zvolený predmet'

    def exec(self, context):
        item_name = self.param

        if item_name == '':
            print('[bold red]Neviem čo chceš použiť.[/bold red]')
            return

        item = get_item_by_name(item_name, context.backpack)
        if item is None:
            print('[bold red]Taký predmet pri sebe nemáš.[/bold red]')
            return

        if USABLE not in item.features:
            print('[bold red]Podľa teba som zrejme blbec, ale naozaj nechápem, načo by to v tejto chvíli bolo dobré.[/bold red]')
            return

        if item.use(context) is False:
            print('[bold red]Podľa teba som zrejme blbec, ale naozaj nechápem, načo by to v tejto chvíli bolo dobré.[/bold red]')
            return

        context.history.append(f'{self.name} {item_name}')
