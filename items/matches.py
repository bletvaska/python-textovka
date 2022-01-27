from helpers import get_item_by_name
from items.door import BURNING, SOAKED
from items.features import MOVABLE, USABLE
from models import Context


def _use(context: Context):
    # scenario

    # 1. usage check
    # v miestnosti su dvere
    door = get_item_by_name("dvere", context.room["items"])
    if door is None:
        print(
            "Zahrkal si zápalkami a presvedčil si sa, že v krabičke je minimálne jedna nepoužitá zápalka. Čo by som tak len s ňou mohol zapáliť?"
        )
        return

    # * dvere su obliate benzinom - su v stave SOAKED
    if door["state"] != SOAKED:
        print("Myslíš, že tie dvere sa len tak chytia od jednej zápalky? Trapny.")
        return

    # ak dvere nie su v miestnosti alebo su v inom stave, tak hlaska na obrazovku
    # pocitadlo == 0?
    # * ak nie, tak znizim o 1 a vypisem hlasku: 'Si skrtol a nic'

    # 2. action
    # aktualizujem dvere
    # * zmeni sa stav na BURNING
    door['state'] = BURNING
    # * zmenim opis: Veľké masívne dubové dvere zachvátené obrovským výdatným plameňom.
    door['description'] = 'Veľké masívne dubové dvere zachvátené obrovským výdatným plameňom.'
    # * zmenim nazov predmetu: horiace dvere
    door['name'] = 'horiace dvere'
    # aktualizujeme zapalky
    # * zapalky uz nie su pouzitelne - odstranim USABLE zo zoznamu ficur
    matches['features'].remove(USABLE)
    # * zmenim opis - Prázdna krabička od zápaliek.
    matches['description'] = 'Prázdna krabička od zápaliek.'

    # 3. render
    print(
        "Škrtol si zápalkou a priložil si ju k nasiaknutým dubovým masívnym dverám. Tie okamžite vzplanuli obrovským plameňom."
    )


matches = {
    "name": "zapalky",
    "description": "Bezpečnostné zápalky. Zrejme kúpené v Bille.",
    "features": [MOVABLE, USABLE],
    "counter": 3,
    "use": _use,
}
