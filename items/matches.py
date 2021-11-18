from .features import MOVABLE, USABLE


def _use(context: dict) -> None:
    raise NotImplementedError('Usage of this item was not yet implemented')


matches = {
    'name': 'zapalky',
    'description': 'Safety match zápalky. Zahrkal si krabičkou a po jej otvorení si našiel len tri.',
    'features': [MOVABLE, USABLE],
    'use': _use
}
