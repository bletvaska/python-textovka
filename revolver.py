from dataclasses import dataclass

from item import Item


@dataclass
class Revolver(Item):
    name: str = 'revolver'
    description: str = 'Sedemkomorový revolver značky Smith&Wesson.'
    # features: list =[MOVABLE, USABLE]
