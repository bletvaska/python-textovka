from dataclasses import dataclass

from models import Context


@dataclass(frozen=True)
class Inventory:
    name: str = "inventar"
    description: str = "vypíše obsah batohu"

    def exec(self, context: Context, name: str):
        if context.backpack == []:
            print("Batoh je prázdny.")
        else:
            print("V batohu máš:")
            for item in context.backpack:
                print(f" * {item['name']}")
