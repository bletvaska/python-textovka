from dataclasses import dataclass, field

from .features import MOVABLE
from .item import Item


@dataclass
class Revolver(Item):
    name: str = 'revolver'
    description: str = 'Sedemkomorový revolver značky Smith&Wesson.'
    features: list[int] = field(default_factory=lambda: [MOVABLE])
