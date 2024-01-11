from commands.command import Command
from helpers import get_item_by_name
from items.features import MOVABLE


class Take(Command):
    name: str = 'vezmi'
    description: str = 'vezme predmet z miestnosti a vloží ho do batohu'

    def exec(self, context):
        if self.param == '':
            print('Neviem, čo chceš zobrať.')
            return

        item = get_item_by_name(self.param, context.current_room.items)

        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        if MOVABLE not in item.features:
            print('Tento predmet sa nedá zobrať.')
            return

        # action
        # odstranim z miestnosti
        context.current_room.items.remove(item)
        # vlozim do batohu
        context.backpack.append(item)
        # render
        print(f'Do batohu si vložil predmet {item.name}.')
