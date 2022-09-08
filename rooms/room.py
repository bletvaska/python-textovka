from dataclasses import dataclass, field

from items.item import Item


@dataclass
class Room:
    name: str
    description: str
    items: list[Item] = field(default_factory=list)  # list[Item] = []

    # exits: list[]
    # north: str
    # south: str
    # east: str
    # west: str
    # up: str
    # down: str

    def show(self):
        print(self.description)
