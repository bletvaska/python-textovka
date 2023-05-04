from pydantic import BaseModel

from features import USABLE, MOVABLE, EXAMINABLE


class Item(BaseModel):
    name: str
    description: str
    features: list = []


class Whip(Item):
    name = 'bic'
    description = 'tvoj neoceniteľný pomocník...!'
    features = [MOVABLE, USABLE]

class EmptySeats(Item):
    name = 'prazdne sedadla'
    description = 'Obvyklé letecké sedadlá.'
    features = [EXAMINABLE]

