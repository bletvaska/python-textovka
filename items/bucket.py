from helpers import get_item_by_name
from items.features import MOVABLE, USABLE
from models import Context


def _use(context: Context):
    # scenario

    # 1. usage check
    # v miestnosti musia byt horiace dvere
    # * name musi byt horiace dvere
    door = get_item_by_name("horiace dvere", context.room["items"])
    # * stav je BURNING
    # * ked nie su, tak: Si si naplnil usta vodou, poprevaloval si si ju v papulke a vyplul si ju naspat do vedra. Setris pre dalsie pouzitie.
    if door is None:
        print(
            "Si si chlipol vody z vedra, poprevaľoval si si ju v papuľke a vypľul si ju naspäť do vedra. Setriš pre ďaľsie použitie."
        )
        return

    # 2. action
    # aktualizujem dvere
    # * zmazem ich z miestnosti
    context.room["items"].remove(door)
    # aktualizujem vedro
    # * zmenim opis: Prázdne vedro.
    bucket["description"] = "12 litrové prázdne vedro."
    # * vyhodim USABLE zo zoznamu vlastnosti
    bucket["features"].remove(USABLE)
    # aktualizujeme miestnost
    # * vytvorime vychod z miestnosti
    context.room["exits"].append("vychod")

    # 3. render
    print(
        "Pristúpil si k horiacim dverám a z bezpečnej vzdialenosti si sa rozohnal a celý obsah vedra si šmaril do plameňa. Voda dokončila dielo skazy a prehorené dubové dvere sa rozpadli. Vyzerá to tak, že si si práve vyrobil východ z miestnosti."
    )


bucket = {
    "name": "vedro",
    "description": "12 litrové vedro plné vody. V niektorých končinách nazývané aj kýbľom.",
    "features": [MOVABLE, USABLE],
    "use": _use,
}
