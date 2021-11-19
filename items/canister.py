from helpers import get_item_by_name
from .door import SOAKED, soaked
from .features import USABLE, MOVABLE


def _use(context: dict) -> None:
    room = context['room']

    # check if door is in the room
    door = get_item_by_name('dvere', room['items'])
    if door is None:
        print('Vzal si kanister do ruky, trošku si zaposiloval a uľavil si si sprostým slovom. Hneď sa cítiš lepšie.')
        return

    # make door soaked
    room['items'].remove(door)
    room['items'].append(soaked)
    # door['description'] = 'Veľké masívne dubové dvere. Len tak niečo a niekto s nimi nepohne, keď sú zamknuté. A to ' \
    #                       'teda sú. A ešte k tomu aj parádne nasiaknuté vysokooktánovým benzínom.'
    # door['state'] = SOAKED

    # update canister
    canister['description'] = 'Veľký 25L kanister. Odšroboval si veko a nadýchol si sa. Ešte pred chvíľou tu bol ' \
                              'určite vysokooktánový benzín. Ale teraz tu už nie je nič.'
    canister['features'].remove(USABLE)

    # render
    print('Odšroboval si vrchnák z kanistra, rozohnal si sa a celý jeho vysokooktánový obsah si vylial '
          'na dubové dvere.')


canister = {
    'name': 'kanister',
    'description': 'Veľký 25L kanister. Odšroboval si veko a nadýchol si sa. Benzín. Vysokooktánový. Isto '
                   'zo Slovnaftu.',
    'features': [MOVABLE, USABLE],
    'use': _use
}
