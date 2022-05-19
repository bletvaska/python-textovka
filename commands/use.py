from dataclasses import dataclass

from commands.command import Command
from context import Context
from helpers import get_item_by_name
from items.features import USABLE


@dataclass
class Use(Command):
    name: str = 'pouzi'
    description: str = 'použije zvolený predmet'

    def exec(self, context: Context):
        # init
        backpack = context.backpack
        room = context.current_room
        name = self.param

        # if no item was entered...
        if name == '':
            print('Neviem, aký predmet chceš použiť.')
            return

        # is the item in room or in backpack?
        item = get_item_by_name(name,
                                room.items + backpack)

        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        # is it movable?
        if USABLE not in item.features:
            print('Tento predmet sa nedá použiť.')
            return

        # usage
        item.use(context)
