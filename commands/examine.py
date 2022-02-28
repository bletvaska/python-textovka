from dataclasses import dataclass
from typing import List

from helpers import get_item_by_name
from .command import Command
from context import Context


@dataclass
class Examine(Command):
    name: str = 'preskumaj'
    # aliases: List[str]
    description: str = 'preskúma zvolený predmet'

    def exec(self, context: Context, param: str):
        # bol zadany nazov predmetu?
        if len(param) == 0:
            print('Neviem čo chceš preskúmať.')
            return

        item = get_item_by_name(param, context.room['items'] + context.backpack)

        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        print(item.description)
