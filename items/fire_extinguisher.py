from helpers import get_item_by_name
from .door import BURNING
from .features import MOVABLE, USABLE


def _use(context: dict) -> None:
    room = context['room']

    # check
    door = get_item_by_name('horiace dvere', room['items'])
    if door is None or door['state'] != BURNING:
        print('Skontroloval si nálepku a plombu na prístroji. Platnosť do 4.7.1957')
        return

    # action
    # remove door from game/room
    room['items'].remove(door)

    # update fire extinguisher
    fire_extinguisher['features'].remove(USABLE)
    fire_extinguisher[
        'description'] = 'Prázdny hasiaci prístroj. Veľmi užitočný ako ťažítko na papiere na pracovnom stole.'

    # make exit from room to west
    room['exits']['east'] = 'garden'

    # render
    print('Ako správny požiarnik si neváhal, odstránil si plombu z hasiaceho prístroja a udrel '
          'si hlavičku o podlahu, čím si odstránil poistku. Nasmeroval si hubicu hasiaceho prístroja '
          'k dverám a začal si hasiť. Plameň sa pod návalom narastajúcej peny uhasil a pod váhou peny '
          'sa dvere rozpadli. Cesta von je voľná. Podskočil si si od radosti.')


fire_extinguisher = {
    'name': 'hasiaci pristroj',
    'description': 'Červená nádoba snehového hasiaceho prístroja. Plomba dáva vedieť, že ešte nebol '
                   'použitý.',
    'features': [MOVABLE, USABLE],
    'use': _use
}
