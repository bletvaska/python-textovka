from dataclasses import dataclass, field

from .item import Item


@dataclass
class HeavyChest(Item):
    name: str = 'tazka okovana truhlica'
    description: str = 'Je vybavená masívnym zámkom...'
