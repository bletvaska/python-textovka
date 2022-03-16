from dataclasses import dataclass, field
from typing import List

from items.features import MOVABLE, USABLE
from .item import Item


@dataclass
class Newspaper(Item):
    name: str = 'noviny'
    description: str = 'dennik sme s autorskou strankou sama marca'
    # features: List[str] = field(default_factory=list)
