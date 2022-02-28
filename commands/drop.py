from dataclasses import dataclass
from typing import List

from helpers import get_item_by_name
from .command import Command
from context import Context


@dataclass
class Drop(Command):
    name: str = 'poloz'
    # aliases: List[str]
    description: str = 'polozi predmet z batohu do miestnosti'

    def exec(self, context: Context, param: str):
        # bol zadany nazov predmetu?
        if param == '':
            print('Neviem, čo chceš položiť.')
            return

        # je v batohu?
        item = get_item_by_name(param, context.backpack)

        if item is None:
            print('Taký predmet pri sebe nemáš.')
            return

        # vymazem z batohu
        context.backpack.remove(item)

        # vlozim do miestnosti
        context.room['items'].append(item)

        # render
        print(f'Do miestnosti si položil predmet {param}.')

        # append to history
        context.history.append(f'{self.name} {param}')
