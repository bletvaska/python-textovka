from dataclasses import dataclass

from commands.command import Command
from context import Context
from helpers import get_item_by_name


@dataclass
class Examine(Command):
    name: str = 'preskumaj'
    description: str = 'bližšie sa pozrie na zvolený predmet'

    def exec(self, context: Context):
        # if no item was entered...
        if self.param == '':
            print('Neviem, co chceš preskúmať.')
            return

        # is the item in room?
        item = get_item_by_name(self.param,
                                context.current_room.items + context.backpack)

        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        # show description
        print(item.description)
