from context import Context
from helpers import get_item_by_name
from .features import USABLE, MOVABLE

name = 'kanister'

description = '10 litrový kanister plný kvalitného slovnafťáckeho vysokooktánového 95% benzínu.'

features = [
    USABLE,
    MOVABLE
]


def use(context: Context):
    # 1. preconditions
    # * dvere su v miestnosti
    door = get_item_by_name('dvere', context.room['items'])
    if door is None:
        print('Zohol si sa, vzal si plny kanister do ruky a zacal si posilovat. Ved predsa plati, ze v zdravom tele '
              'zdravy duch.')
        return

    # 2. action
    # * polejeme dvere
    #   - aktualizujeme dvere - description, name
    door.description = 'Veľké masívne drevené dvere nasiaknuté kvalitným vysokooktánovým 95% benzínom.'
    door.state = door.SOAKED_STATE

    # * aktualizujeme kanister
    #   - kanister uz nebude USABLE
    features.remove(USABLE)
    #   - aktualizujeme description
    global description
    description = '10 litrový prázdny kanister na benzín.'

    # 3. render
    print('Odsroboval si vrchnak kanistru a cely jeho obsah si vylial na velke masivne dvere. Doteraz tu bol taky '
          'pokoj a klud, ale odteraz sa vzduchom rozplyva vona 95% kvalitneho vysokooktanoveho benzinu z ruska.')
