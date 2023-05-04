from pydantic import BaseModel

from features import USABLE, MOVABLE


class Item(BaseModel):
    name: str
    description: str
    features: list = []


class Whip(Item):
    name = 'bic'
    description = 'tvoj neoceniteľný pomocník...!'
    features = [MOVABLE, USABLE]
