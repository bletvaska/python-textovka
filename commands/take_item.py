from dataclasses import dataclass
from helpers import get_item_by_name
from items.features import MOVABLE

from models import Context


@dataclass(frozen=True)
class TakeItem:
    name: str = "vezmi"
    description: str = "vezme predmet z miestnosti a vloží si ho do batohu"

    def exec(self, context: Context, name: str):
        # if no item was given, then quit
        if len(name) == 0:
            print("Neviem, aký predmet chceš vziať.")
            return

        item = get_item_by_name(name, context.room["items"])

        # if item was not found, then quit
        if item is None:
            print("Taký predmet tu nikde nevidím.")
            return

        # if item is now movable, then quit
        if MOVABLE not in item["features"]:
            print("Tento predmet sa nedá zobrať.")
            return

        # action
        context.room["items"].remove(item)
        context.backpack.append(item)
        print(f"Do batohu si vložil predmet {name}.")
