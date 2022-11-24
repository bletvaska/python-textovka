from dataclasses import dataclass, field


@dataclass
class Room:
    name: str
    description: str
    items: list = field(default_factory=list)
    exits: dict = field(default_factory=dict)
