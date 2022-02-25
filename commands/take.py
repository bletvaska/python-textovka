from dataclasses import dataclass
from typing import List

from helpers import get_item_by_name
from items.features import MOVABLE
from .command import Command
from context import Context


@dataclass
class Take(Command):
    name: str = 'vezmi'
    # aliases: List[str]
    description: str = 'zoberie predmet z miestnosti a vloží ho do batohu'

    def exec(self, context: Context, param: str):
        # bol zadany nazov predmetu?
        if param == '':
            print('Neviem, čo chceš vziať.')
            return

        # je v miestnosti?
        item = get_item_by_name(param, context.room['items'])
        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        # je prenositelny?
        if MOVABLE not in item.features:
            print('Tento predmet sa nedá zobrať.')
            return

        # vymazem z miestnosti
        context.room['items'].remove(item)

        # vlozim do batohu
        context.backpack.append(item)

        # render
        print(f'Do batohu si si vložil predmet {param}.')
