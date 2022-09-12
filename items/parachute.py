from dataclasses import dataclass, field

from .features import MOVABLE, USABLE
from .item import Item


@dataclass
class Parachute(Item):
    name: str = 'padak'
    description: str = 'Obyčajný padák MADE IN U.S.A. 1933'
    features: list[str] = field(default_factory=lambda: [MOVABLE, USABLE])
