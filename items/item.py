from dataclasses import dataclass, field
from typing import List


@dataclass
class Item:
    name: str
    description: str
    features: List[int] = field(default_factory=list)
