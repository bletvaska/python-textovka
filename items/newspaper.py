import random
from items.features import MOVABLE, USABLE
from models import Context


def _use(context: Context):
    print("Fúúúú... Nové košické tajmsy. Kuknice še, co píšu...")

    headlines = (
        "Diaľnica D1 je podľa najnovších odhadov naplánovaná na dokončenie v roku 2010. Hmm... Tu mi niečo nesedí...",
        "Róbert F. sa vyjadril, že opúšťa politiku. Zase. Na týždeň.",
        "Dojče telekom zvyšuje platy... Zle čítam... RAM-ky. Dvojnásobne.",
        "Mirek sa stal prezidentom. Zase.",
    )

    print(random.choice(headlines))


newspaper = {
    "name": "noviny",
    "description": "Košické tajmsy. Dnešné, ešte teplé vydanie.",
    "features": [MOVABLE, USABLE],
    "use": _use,
}
