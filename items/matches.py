from dataclasses import dataclass

from items.features import MOVABLE, USABLE


@dataclass
class Matches:
    name = 'zapalky'
    description = 'Štandardné zápalky. Tri.'
    features = [MOVABLE, USABLE]
