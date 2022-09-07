from dataclasses import dataclass, field

from .features import USABLE, MOVABLE
from .item import Item


@dataclass
class Newspaper(Item):
    name: str = 'noviny'
    description: str = 'Čerstvé vydanie Denníka N.'
    features: list[int] = field(default_factory=lambda: [MOVABLE, USABLE])
