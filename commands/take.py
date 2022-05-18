from dataclasses import dataclass

from helpers import get_item_by_name
from items.features import MOVABLE


@dataclass
class Take:
    name: str = 'vezmi'
    description: str = 'vezme predmet z miestnosti a vloží si ho do batohu'

    def exec(self, line, room, backpack):
        # extraction of item to vezmi
        name = line.split('vezmi')[1].lstrip()

        # if no item was entered...
        if name == '':
            print('Neviem, co chceš zobrať.')

        else:
            # is the item in room?
            item = get_item_by_name(name, room.items)

            if item is None:
                print('Taký predmet tu nevidím.')

            else:
                # is it movable?
                if MOVABLE not in item.features:
                    print('Tento predmet sa nedá zobrať.')

                else:
                    # vezmi item
                    # vezmi item z miestnosti
                    room.items.remove(item)

                    # add item to backpack items
                    backpack.append(item)

                    # render
                    print(f'Predmet {item.name} si si vložil do batohu.')
