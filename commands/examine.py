import states
from commands.command import Command
from helpers import get_item_by_name
from items.features import EXAMINABLE


class Examine(Command):
    name: str = 'preskumaj'
    description: str = 'zobrazí informácie o zvolenom predmete'

    def exec(self, context):
        if self.param == '':
            print('Neviem, čo chceš preskúmať.')
            return

        item = get_item_by_name(self.param, context.current_room.items)

        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        # action
        print(item.description)

        # is item examinable?
        if EXAMINABLE in item.features:
            input('Moment... Niečo tam je...')
            item.examine(context)
