from dataclasses import dataclass

from .item import Item


@dataclass
class Bucket(Item):
    name: str = 'vedro'
    description: str = 'Vedro plné vody.'
