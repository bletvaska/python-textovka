from dataclasses import dataclass

from helpers import get_item_by_name
from .command import Command


@dataclass
class Drop(Command):
    name: str = 'poloz'
    description: str = 'vyberie zvolený predmet z batohu a položí ho do aktuálnej miestnosti'

    def exec(self, context):
        if self.parameter == '':
            print('Neviem čo chceš položiť.')
        else:
            item = get_item_by_name(self.parameter, context.backpack)

            if item is None:
                print('Taký predmet pri sebe nemáš.')
            else:
                # remove item from backpack
                context.backpack.remove(item)

                # insert item to current room
                context.current_room.items.append(item)

                # render
                print(f'Do miestnosti si položil predmet {item.name}.')

        # solution with try-except
        # try:
        #     # get item by name from backpack
        #     item = get_item_by_name(self.parameter, context.backpack)
        #
        #     # remove item from backpack
        #     context.backpack.remove(item)
        #
        #     # insert item to current room
        #     context.current_room.items.append(item)
        #
        #     # render
        #     print(f'Do miestnosti si položil predmet {item.name}.')
        # except EmptyParameter:
        #     print('Neviem čo chceš položiť.')
        # except ItemNotFound:
        #     print('Taký predmet pri sebe nemáš.')
