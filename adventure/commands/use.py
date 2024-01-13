from rich import print

from adventure.helpers import get_item_by_name
from adventure.items.features import USABLE
from .command import Command


class Use(Command):
    name: str = 'pouzi'
    description: str = 'použije zvolený predmet'

    def exec(self, context):
        # if no item was entered
        if self.param == '':
            print("Neviem, čo chceš použiť.")
            return

        # search for item in backpack
        item = get_item_by_name(self.param, context.backpack)

        # was item found?
        if item is None:
            print('Taký predmet pri sebe nemáš.')
            return

        # is item usable?
        if USABLE not in item.features or item.on_use(context) is False:
            print('[bold red]Podľa teba som zrejme blbec, ale naozaj nechápem, načo by to v tejto chvíli bolo '
                  'dobré.[/bold red]')
        else:
            # append command to history
            context.history.append(f'{self.name} {self.param}')
