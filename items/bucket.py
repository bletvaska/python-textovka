from context import Context
from helpers import get_item_by_name
from .features import USABLE, MOVABLE

name = 'vedro'

description = 'Vedro plné vody.'

features = [
    USABLE,
    MOVABLE
]


def use(context: Context):
    # 1. preconditions
    # som v miestnosti s dverami?
    # horia dvere?
    door = get_item_by_name('horiace dvere', context.room['items'])
    if door is None:
        print('Nabral si si vodu do dlaní, chlipol si si, poprevaľoval si si vodu v papuľke a vypľul si ju naspäť. Na '
              'neskôr.')
        return

    # 2. action
    # aktualizujem vedro
    # - nebude USABLE
    features.remove(USABLE)
    # - aktualizujem opis (prazdne vedro)
    global description
    description = 'Prázdne vedro'
    # aktualizujem dvere
    # - odstranim dvere z hry (zmazem ich z room['items']
    context.room['items'].remove(door)
    # otvorim prechod do novej miestnosti
    # - na zapad -> garden
    context.room['exits']['west'] = 'záhradka'

    # 3. render
    print('Masaker. ta si zahasil poziar a sa dvere rozpadli.')
