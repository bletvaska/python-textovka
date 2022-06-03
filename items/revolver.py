from dataclasses import dataclass, field

from items.features import MOVABLE


@dataclass
class Revolver:
    name: str = 'revolver'
    description: str = 'Štandardný revolver značky Smis-end-Weson'
    features: list[int] = field(default_factory=lambda: [MOVABLE])
