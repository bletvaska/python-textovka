from dataclasses import dataclass, field

from items.features import USABLE, MOVABLE
from items.item import Item


@dataclass
class Bucket(Item):
    name: str = 'vedro'
    description: str = 'Vedro plné vody. Ťažko povedať, či aj pitnej.'
    features: list[int] = field(default_factory=lambda: [MOVABLE, USABLE])
