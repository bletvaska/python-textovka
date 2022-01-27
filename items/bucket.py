from items.features import MOVABLE, USABLE
from models import Context


def _use(context: Context):
    # scenario

    # 1. usage check
    # v miestnosti musia byt horiace dvere
    # * name musi byt horiace dvere
    # * stav je BURNING
    # * ked nie su, tak: Si si naplnil usta vodou, poprevaloval si si ju v papulke a vyplul si ju naspat do vedra. Setris pre dalsie pouzitie.

    # 2. action
    # aktualizujem dvere
    # * zmazem ich z miestnosti
    # aktualizujem vedro
    # * zmenim opis: Prázdne vedro.
    # * vyhodim USABLE zo zoznamu vlastnosti

    # 3. render
    print('Pristúpil si k horiacim dverám a z bezpečnej vzdialenosti si sa rozohnal a celý obsah vedra si šmaril do plameňa. Voda dokončila dielo skazy a prehorené dubové dvere sa rozpadli. Vyzerá to tak, že si si práve vyrobil východ z miestnosti.')


bucket = {
    "name": "vedro",
    "description": "12 litrové vedro plné vody. V niektorých končinách nazývané aj kýbľom.",
    "features": [MOVABLE, USABLE],
    "use": _use,
}
