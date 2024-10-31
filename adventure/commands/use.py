from helpers import get_item_by_name
from items.features import USABLE
from .command import Command


class Use(Command):
    name: str = 'pouzi'
    description: str = 'použije zvolený predmet'

    def exec(self, context, param):
        if param == '':
            print('Neviem, čo chceš použiť.')
            return

        item = get_item_by_name(param, context.backpack)
        if item is None:
            print('Taký predmet pri sebe nemáš.')
            return

        if USABLE not in item.features:
            print('Podľa teba som zrejme blbec, ale naozaj nechápem, načo by to v tejto chvíli bolo dobré.')
            return

        was_used = item.use(context)
        if not was_used:
            print('Podľa teba som zrejme blbec, ale naozaj nechápem, načo by to v tejto chvíli bolo dobré.')
        else:
            context.history.append(f'{self.name} {param}')
