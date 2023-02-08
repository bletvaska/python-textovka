from helpers import get_item_by_name
from .command import Command


class Drop(Command):
    name = 'poloz'
    description = 'vyberie zvolený predmet z batohu a položí ho do aktuálnej miestnosti'

    def exec(self, context):
        # if no item was entered
        if self.param == '':
            print('Neviem, čo chceš položiť.')
            return

        # search for item
        item = get_item_by_name(self.param, context.backpack)

        # not found
        if item is None:
            print('Taký predmet pri sebe nemáš.')
            return

        # take item
        context.backpack.remove(item)
        context.current_room.items.append(item)

        # render
        print(f'Do miestnosti si položil predmet {item.name}.')
