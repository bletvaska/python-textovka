from .features import MOVABLE, USABLE


def _use(context: dict) -> None:
    raise NotImplementedError('Usage of this item was not yet implemented')


fire_extinguisher = {
    'name': 'hasiaci pristroj',
    'description': 'Červená nádoba snehového hasiaceho prístroja. Plomba dáva vedieť, že ešte nebol '
                   'použitý.',
    'features': [MOVABLE, USABLE],
    'use': _use
}
