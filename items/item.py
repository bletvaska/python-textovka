from dataclasses import dataclass, field


@dataclass
class Item:
    name: str
    description: str
    features: list = field(default_factory=list)
