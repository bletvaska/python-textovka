from helpers import get_item_by_name
from .door import SOAKED, BURNING
from .features import MOVABLE, USABLE


def _use(context: dict) -> None:
    # check
    door = get_item_by_name('dvere', context['room']['items'])
    if door is not None and door['state'] != SOAKED:
        print('Priložil si si krabičku k ušku a zahrkal si s ňou. Stále sa v nej niečo nachádza.')
        return

    # action
    # inactivate usable matches
    matches['features'].remove(USABLE)

    # door starts burning
    door['description'] = 'Veľké masívne dubové dvere zachvátené obrovským výdatným plameňom.'
    door['name'] = 'horiace dvere'
    door['state'] = BURNING

    # render
    print('Škrtol si zápalkou a priložil si ju k nasiaknutým dubovým masívnym dverám. Tie okamžite '
          'vzplanuli obrovským plameňom.')


matches = {
    'name': 'zapalky',
    'description': 'Safety match zápalky. Zahrkal si krabičkou a po jej otvorení si našiel len tri.',
    'features': [MOVABLE, USABLE],
    'use': _use
}
