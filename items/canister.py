from dataclasses import dataclass

from .item import Item


@dataclass
class Canister(Item):
    name: str = 'kanister'
    description: str = 'Vysokooktánový benzín tvorí obsah tohto kanistra. Kvalitka za rozumnú cenu.'
