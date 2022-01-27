from dataclasses import dataclass
import random
from helpers import get_item_by_name
from items.door import SOAKED
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

        elif name == 'kanister':
            # scenario
            canister = item

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

        elif name == 'zapalky':
            print('ta skrtam zapalky a podpalujem dvere nasiaknute benzinom')

        elif name == 'vedro':
            print('ta hasim horiace dvere vedrom s vodou a tie sa rozpadnu')

        else:
            raise NotImplementedError(f'Usage of item {name} was not yet implemented.')
