from dataclasses import dataclass

from commands.command import Command
from helpers import get_item_by_name


@dataclass
class Examine(Command):
    name: str = 'preskumaj'
    description: str = 'zobrazí opis predmetu'

    def exec(self, context, line: str):
        name = line.split('preskumaj')[1].lstrip()

        # check if there is something to examine ;)
        if name == '':
            print('Neviem, aký predmet chceš preskúmať.')
        else:
            # check if item is in backpack
            item = get_item_by_name(name, context.backpack)
            if item is None:
                print('Taký predmet pri sebe nemáš.')
            else:
                print(item.description)
