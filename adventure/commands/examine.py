from helpers import get_item_by_name
from items.features import EXAMINABLE
from states import PLAYING
from .command import Command


class Examine(Command):
    name: str = 'preskumaj'
    description: str = 'zobrazí informácie o zvolenom predmete'

    def exec(self, context):
        item_name = self.param

        # if not item was entered
        if item_name == '':
            print('Neviem, čo chceš preskúmať.')
            return

        # if not found
        item = get_item_by_name(item_name, context.current_room.items + context.backpack)
        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        # when found
        context.history.append(f'{self.name} {item_name}')

        print(item.description)

        if EXAMINABLE in item.features:
            if context.game_state == PLAYING:
                input('Pozrel si sa trošku bližšie a...')
            item.examine(context)
