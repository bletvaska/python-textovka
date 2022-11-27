from helpers import get_item_by_name
from items.features import USABLE
from .command import Command


class Use(Command):
    name = 'pouzi'
    description = 'použije zvolený predmet'

    def exec(self, context):
        # if no item was entered
        if self.param == '':
            print("Neviem, čo chceš použiť.")
            return

        # search for item in room
        item = get_item_by_name(self.param, context.current_room.items + context.backpack)

        # was item found?
        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        # is item usable?
        if USABLE not in item.features:
            print('Tento predmet sa nedá použiť.')
            return

        # use item
        status = item.use(context)
        if status is False:
            print('Podľa teba som zrejme blbec, ale naozaj nechápem, na čo by to v tejto chvíli bolo dobré.')
        else:
            # append command to history
            context.history.append(f'{self.name} {self.param}')
