from helpers import get_item_by_name
from items.features import USABLE
from .command import Command


class Use(Command):
    name = 'pouzi'
    description = 'použije zvolený predmet'

    def exec(self, context):
        # when no param was given
        # len(self.param) == 0
        if self.param == '':
            print('Neviem, aký predmet chceš použiť.')
            return

        # find item by name
        item = get_item_by_name(self.param, context.backpack)
        if item == None:
            print('Taký predmet pri sebe nemáš.')
            return

        # is item usable
        if USABLE not in item.features:
            print('Tento predmet sa nedá použiť.')
            return

        # action
        print('Print pouzivam predmet')
