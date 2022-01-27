from dataclasses import dataclass
import random
from helpers import get_item_by_name
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

        # read newspaper
        if name == "noviny":
            print("Fúúúú... Nové košické tajmsy. Kuknice še, co píšu...")

            headlines = (
                'Diaľnica D1 je podľa najnovších odhadov naplánovaná na dokončenie v roku 2010. Hmm... Tu mi niečo nesedí...',
                'Róbert F. sa vyjadril, že opúšťa politiku. Zase. Na týždeň.',
                'Dojče telekom zvyšuje platy... Zle čítam... RAM-ky. Dvojnásobne.',
                'Mirek sa stal prezidentom. Zase.'
            )

            print(random.choice(headlines))

        else:
            print(f"POuzivam dajako predmet {name}.")
