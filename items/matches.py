from items.features import MOVABLE, USABLE
from models import Context


def _use(context: Context):
    # scenario

    # 1. usage check
    # v miestnosti su dvere
    # * dvere su obliate benzinom - su v stave SOAKED
    # ak dvere nie su v miestnosti alebo su v inom stave, tak hlaska na obrazovku

    # 2. action
    # aktualizujem dvere
    # * zmeni sa stav na BURNING
    # * zmenim opis: Veľké masívne dubové dvere zachvátené obrovským výdatným plameňom.
    # * zmenim nazov predmetu: horiace dvere
    # aktualizujeme zapalky
    # * zapalky uz nie su pouzitelne - odstranim USABLE zo zoznamu ficur
    # * zmenim opis - Prázdna krabička od zápaliek.

    # 3. render
    print('Škrtol si zápalkou a priložil si ju k nasiaknutým dubovým masívnym dverám. Tie okamžite vzplanuli obrovským plameňom.')


matches = {
    "name": "zapalky",
    "description": "Bezpečnostné zápalky. Zrejme kúpené v Bille.",
    "features": [MOVABLE, USABLE],
    "use": _use,
}
