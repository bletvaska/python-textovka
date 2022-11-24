from dataclasses import dataclass


@dataclass
class Room:
    name: str
    description: str
    items: list
    exits: list  # TODO ????
