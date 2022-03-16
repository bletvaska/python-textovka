from dataclasses import dataclass

from .features import USABLE, MOVABLE
from .item import Item


@dataclass
class Canister(Item):
    name: str = 'kanister'
    description: str = 'Vysokooktánový benzín tvorí obsah tohto kanistra. Kvalitka za rozumnú cenu.'

    def __post_init__(self):
        self.features += [MOVABLE, USABLE]
