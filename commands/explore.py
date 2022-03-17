from dataclasses import dataclass

from context import Context
from utils import get_item_by_name
from .command import Command


@dataclass
class Explore(Command):
    name: str = 'preskumaj'
    description: str = 'zobrazí opis predmetu'

    def __post_init__(self):
        self.aliases += ['preskumat', 'examine']

    def exec(self, context: Context, arg: str):
        item_name = arg
        backpack = context.backpack['items']
        room = context.room

        # is there name given?
        if item_name == '':
            print('Neviem čo chceš preskúmať.')
            return

        # find item by name
        item = get_item_by_name(item_name, room.items + backpack)

        # if no such item available
        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        # explore item
        print(item.description)
