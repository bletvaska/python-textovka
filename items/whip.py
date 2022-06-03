from dataclasses import dataclass, field
from typing import List

from items.features import MOVABLE


@dataclass
class Whip:
    name: str = 'bic'
    description: str = 'Tvoj neoceniteľný kamarát na každom jednom dobrodužstve.'
    features: List[int] = field(default_factory=lambda: [MOVABLE])
