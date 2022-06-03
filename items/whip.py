from dataclasses import dataclass, field

from items.features import MOVABLE


@dataclass
class Whip:
    name: str = 'bic'
    description: str = 'Tvoj neoceniteľný kamarát na každom jednom dobrodužstve.'
    features: list[int] = field(default_factory=lambda: [MOVABLE])
