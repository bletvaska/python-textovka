from helpers import get_item_by_name
from items.features import EXAMINABLE
from .command import Command


class Examine(Command):
    name: str = 'preskumaj'
    description: str = 'zobrazí informácie o zvolenom predmete'

    def exec(self, context):
        # if no item was entered
        if self.param == '':
            print("Neviem, čo chceš preskúmať.")
            return

        # search for item
        item = get_item_by_name(self.param, context.backpack + context.current_room.items)

        # was found?
        if item is None:
            print("Taký predmet tu nikde nevidím.")
            return

        # render
        print(item.description)

        # is item examinable?
        if EXAMINABLE in item.features:
            item.on_examine(context)

        # append command to history
        context.history.append(f'{self.name} {self.param}')
