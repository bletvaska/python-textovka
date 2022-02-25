from dataclasses import dataclass
from typing import List

from helpers import get_item_by_name
from items.features import USABLE
from .command import Command
from context import Context


@dataclass
class Use(Command):
    name: str = 'pouzi'
    # aliases: List[str]
    description: str = 'použije zvolený predmet'

    def exec(self, context: Context, param: str):
        # bol zadany nazov predmetu?
        if param == '':
            print('Neviem, čo chceš použiť.')
            return

        # je v miestnosti alebo batohu?
        item = get_item_by_name(param, context.room['items'] + context.backpack)
        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        # je pouzitelny?
        if USABLE not in item.features:
            print('Tento predmet sa nedá použiť.')
            return

        # use item
        print(f'Snažím sa použiť predmet {param}.')
        item.use()
