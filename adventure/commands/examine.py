from helpers import get_item_by_name
from items.features import EXAMINABLE
from .command import Command


class Examine(Command):
    name: str = 'preskumaj'
    description: str = 'zobrazí informácie o zvolenom predmete'

    def exec(self, context, param):
        if param == '':
            print('Neviem, čo chceš preskúmať.')
            return

        item = get_item_by_name(param, context.current_room.items + context.backpack)
        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        # action
        print(item.description)

        # is item examinable?
        if EXAMINABLE in item.features:
            input('Pozrel si sa trošku bližšie a...')
            item.examine(context)

            context.history.append(f'{self.name} {param}')
