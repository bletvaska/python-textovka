from dataclasses import dataclass

from .item import Item


@dataclass
class Newspaper(Item):
    name: str = 'noviny'
    description: str = 'Čerstvé vydanie Denníka N.'
    # features: list =[MOVABLE, USABLE]
