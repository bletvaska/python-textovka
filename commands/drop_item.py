from dataclasses import dataclass
from helpers import get_item_by_name

from models import Context


@dataclass(frozen=True)
class DropItem:
    name: str = "poloz"
    description: str = "vyloží predmet z batohu do miestnosti"

    def exec(self, context: Context, name: str):
        # if no item was given, then quit
        if len(name) == 0:
            print("Neviem, aký predmet chceš položiť.")
            return

        # find item by name
        item = get_item_by_name(name, context.backpack)

        # if no item found, then quit
        if item is None:
            print("Taký predmet pri sebe nemáš.")
            return

        # poloz ho do miestnosti
        context.room["items"].append(item)

        # zmaz ho z batohu
        context.backpack.remove(item)

        # render
        print(f"Do miestnosti si vyložil predmet {name}.")
