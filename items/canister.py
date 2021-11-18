from .features import USABLE, MOVABLE


def _use(context: dict) -> None:
    raise NotImplementedError('Usage of this item was not yet implemented')


canister = {
    'name': 'kanister',
    'description': 'Veľký 25L kanister. Odšroboval si veko a nadýchol si sa. Benzín. Vysokooktánový. Isto '
                   'zo Slovnaftu.',
    'features': [MOVABLE, USABLE],
    'use': _use
}
