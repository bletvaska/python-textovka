from dataclasses import dataclass, field
from typing import List

from items.item import Item


@dataclass
class Room:
    name: str
    description: str
    items: List[Item] = field(default_factory=list)
    west: str = None
    east: str = None
    north: str = None
    south: str = None

    def show(self):
        """
        {description}

        Vidíš:
          {items}
        """

        # print room description
        print(self.description)
        print()

        # print items in room
        if self.items != []:
            print('Vidíš:')
            for item in self.items:
                print(f'  {item.name}')
        else:
            print('Nevidíš tu nič zaujímavé.')

        # print exits from the room
        # Možné východy z miestnosti:
        #   východ
        #
        # Z miestnosti nevedú žiadne východy.
