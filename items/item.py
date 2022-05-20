from dataclasses import dataclass


@dataclass
class Item:
    name: str
    description: str
    features: list[int]