from commands.command import Command
from helpers import get_item_by_name
from items.features import USABLE


class Use(Command):
    name: str = 'pouzi'
    description: str = 'použije zvolený predmet z batohu'

    def exec(self, context):
        # if no params
        if self.param == '':
            print('Neviem čo chceš použiť.')
            return

        # search item by name in backpack
        item = get_item_by_name(self.param, context.backpack)

        # if not found
        if item is None:
            print('Taký predmet pri sebe nemáš.')
            return

        # is USABLE?
        if USABLE not in item.features or item.use(context) == False:
            print('Podľa teba som zrejme blbec, ale naozaj nechápem, na čo by to v tejto chvíli bolo dobré.')
            return

        # use item
        # if item.use(context) == False:
        #     print('Podľa teba som zrejme blbec, ale naozaj nechápem, na čo by to v tejto chvíli bolo dobré.')


