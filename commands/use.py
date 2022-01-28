from dataclasses import dataclass
import random
from helpers import get_item_by_name
from items.door import SOAKED
from items.features import USABLE

from models import Context


@dataclass
class UseItem:
    name: str = "pouzi"
    description: str = "použije zvolený predmet"

    def exec(self, context: Context, name: str):
        # if no item was given, then quit
        if len(name) == 0:
            print("Neviem, čo chceš použiť.")
            return

        # find item by name
        item = get_item_by_name(name, context.backpack + context.room["items"])

        # if no item found, then quit
        if item is None:
            print("Taký predmet tu nikde nevidím.")
            return

        # if item is not usable, then quit
        if USABLE not in item["features"]:
            print("Tento predmet sa nedá použiť.")
            return

        # action
        context.history.append(f'pouzi {name}')

        # read newspaper
        item['use'](context)

