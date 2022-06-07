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
        Prints the content of the location.
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

        # # print exits from the room
        # if self.north is None and self.south is None and self.east is None and self.west is None:
        #     print('Z miestnosti nevedú žiadne východy.')
        # else:
        #     print('Možné východy z miestnosti:')
        #     if self.north is not None:
        #         print('  sever')
        #     if self.east is not None:
        #         print('  východ')
        #     if self.west is not None:
        #         print('  západ')
        #     if self.south is not None:
        #         print('  juh')

        # print exits from the room
        directions = []
        if self.north is not None:
            directions.append('sever')
        if self.south is not None:
            directions.append('juh')
        if self.east is not None:
            directions.append('východ')
        if self.west is not None:
            directions.append('západ')

        if len(directions) == 0:
            print('Z miestnosti nevedú žiadne východy.')
        else:
            if len(directions) == 1:
                print(f'Môžeš ísť na {directions[0]}.')
            else:
                print('Môžeš ísť na',
                      ', '.join(directions[:-1]),
                      f'a {directions[-1]}.')

            # for direction in directions:
            #     print(f'  {direction}')

        # directions = {
        #     'north': None,
        #     'south': None,
        #     'east': None,
        #     'west': None,
        # }

        # for direction in directions:
