from context import Context
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

    # 2. action
    # aktualizujem vedro
    # - nebude USABLE
    # - aktualizujem opis (prazdne vedro)
    # aktualizujem dvere
    # - odstranim dvere z hry (zmazem ich z room['items']
    # otvorim prechod do novej miestnosti
    # - na zapad -> garden

    # 3. render
    print('masaker. ta si zahasil poziar a sa dvere rozpadli.')
