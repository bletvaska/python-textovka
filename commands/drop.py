from commands.command import Command
from helpers import get_item_by_name


class Drop(Command):
    name: str = 'poloz'
    description: str = 'vyberie zvolený predmet z batohu a položí ho do aktuálnej miestnosti'

    def exec(self, context):
        if self.param == '':
            print('Neviem, čo chceš položiť.')
            return

        item = get_item_by_name(self.param, context.backpack)

        if item is None:
            print('Taký predmet pri sebe nemáš.')
            return

        # action
        # odstranim z batohu
        context.backpack.remove(item)
        # vlozim do miestnosti
        context.current_room.items.append(item)
        # render
        print(f'Do miestnosti si položil {item.name}.')
