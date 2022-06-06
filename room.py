from dataclasses import dataclass, field
from typing import List

from items.item import Item


@dataclass
class Room:
    name: str
    description: str
    items: List[Item] = field(default_factory=list)

    def show(self):
        """
        {description}

        Vidíš:
          {items}
        """
