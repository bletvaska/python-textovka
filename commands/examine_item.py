from dataclasses import dataclass
from helpers import get_item_by_name

from models import Context


@dataclass(frozen=True)
class ExamineItem:
    name: str = "preskumaj"
    description: str = "vypíše opis daného predmetu"

    def exec(self, context: Context, name: str):
        # if no item was given, then quit
        if len(name) == 0:
            print("Neviem, čo chceš preskúmať.")
            return

        item = get_item_by_name(name, context.backpack + context.room["items"])

        # if item was not found, then quit
        if item is None:
            print("Tento predmet tu nikde nevidím.")
            return

        # action
        print(item["description"])
