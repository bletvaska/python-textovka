from dataclasses import dataclass

from context import Context
from items.features import MOVABLE
from utils import get_item_by_name
from .command import Command


@dataclass
class Take(Command):
    name: str = 'vezmi'
    description: str = 'vezme predmet z miestnosti a vloží si ho do batohu'

    def __post_init__(self):
        self.aliases += ['take', 'zober']

    def exec(self, context: Context, arg: str):
        item_name = arg
        room = context.room
        backpack = context.backpack['items']

        # is there name given?
        if item_name == '':
            print('Neviem čo chceš zobrať.')
            return

        item = get_item_by_name(item_name, room['items'])

        # if no such item in room
        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        # is item movable?
        if MOVABLE not in item.features:
            print('Tento predmet sa nedá zobrať.')
            return

        # is backpack full?
        if len(backpack) >= context.backpack['capacity']:
            print('Batoh je plný.')
            return

        # take item
        context.history.append(f'VEZMI {item_name}')

        # remove item from room
        room['items'].remove(item)

        # drop item in the backpack
        backpack.append(item)

        # print out
        print(f'Predmet {item.name} si si vložil do batohu.')
