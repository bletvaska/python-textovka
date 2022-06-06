from dataclasses import dataclass

from commands.command import Command
from context import Context
from helpers import get_item_by_name


@dataclass
class Examine(Command):
    name: str = 'preskumaj'
    description: str = 'zobrazí opis predmetu'

    def exec(self, context: Context, name: str):
        # check if there is something to examine ;)
        if name == '':
            print('Neviem, aký predmet chceš preskúmať.')
        else:
            # check if item is in backpack
            item = get_item_by_name(name, context.backpack + context.current_room.items)
            if item is None:
                print('Taký predmet tu nikde nevidím.')
            else:
                print(item.description)
