from helpers import get_item_by_name
from items.door import SOAKED
from models import Context
from .features import MOVABLE, USABLE


def _use(context: Context):
    # scenario

    # 1. usability check
    # * v miestnosti musia byt dvere!
    #   ak tam dvere nie su, vypise sa na obrazovku ftipna sprava: Vzal si kanister do ruky, trošku si zaposiloval a uľavil si si sprostým slovom (ako mirek). Hneď sa cítiš lepšie.
    door = get_item_by_name('dvere', context.room['items'])
    if door is None:
        print('Vzal si kanister do ruky, trošku si zaposiloval a uľavil si si sprostým slovom (ako mirek). Hneď sa cítiš lepšie.')
        return

    # 2. action
    # aktualizacia dveri
    # * zmeni sa opis na obliate dvere
    door['description'] = 'Veľké masívne dubové dvere. Len tak niečo a niekto s nimi nepohne, keď sú zamknuté. A to teda sú. A ešte k tomu aj parádne nasiaknuté vysokooktánovým benzínom.'
    # * zmeni sa stav dveri z NORMAL na SOAKED
    door['state'] = SOAKED

    # aktualizujeme kanister
    # * stane sa nepouzitelnym - vymaze sa USABLE zo zoznamu ficur
    canister['features'].remove(USABLE)
    # * zmenime mu opis -
    canister['description'] = 'Veľký 10L kanister. Odšroboval si veko a nadýchol si sa. Ešte pred chvíľou tu bol určite vysokooktánový benzín. Ale teraz tu už nie je nič.'

    # 3. render
    print('Odšroboval si vrchnák z kanistra, rozohnal si sa a celý jeho vysokooktánový obsah si vylial na dubové dvere.')


canister = {
    "name": "kanister",
    "description": "Veľký 10 litrový kanister žltej farby. Značka: plný vysokooktánového výborne horľavého benzínu.",
    "features": [MOVABLE, USABLE],
    "use": _use,
}
