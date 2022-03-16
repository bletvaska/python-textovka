from dataclasses import dataclass, field

from directions import Directions


@dataclass
class Room:
    name: str
    description: str
    items: list = field(default_factory=list)
    exits: dict = field(default_factory=dict)

    def __post_init__(self):
        if Directions.EAST not in self.exits:
            self.exits[Directions.EAST] = None
        if Directions.WEST not in self.exits:
            self.exits[Directions.WEST] = None
        if Directions.NORTH not in self.exits:
            self.exits[Directions.NORTH] = None
        if Directions.SOUTH not in self.exits:
            self.exits[Directions.SOUTH] = None
