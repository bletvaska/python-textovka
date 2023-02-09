from helpers import get_item_by_name
from items.features import USABLE
from .command import Command


class Use(Command):
    name = 'pouzi'
    description = 'použije predmet z batohu'

    def exec(self, context):
        # if no item was entered
        if self.param == '':
            print('Neviem, čo chceš použiť.')
            return

        # search for item
        item = get_item_by_name(self.param, context.backpack)

        # not found
        if item is None:
            print('Taký predmet pri sebe nemáš.')
            return

        # is item usable?
        # if USABLE not in item.features:
        #     print('Podľa teba som zrejme blbec, ale naozaj nechápem, na čo by to v tejto chvíli bolo dobré.')
        #     return

        # use item
        success = item.use(context)
        if success is False:
            print('Podľa teba som zrejme blbec, ale naozaj nechápem, na čo by to v tejto chvíli bolo dobré.')
