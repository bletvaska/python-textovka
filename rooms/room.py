from dataclasses import dataclass, field

from items.item import Item


@dataclass
class Room:
    name: str
    description: str
    items: list[Item] = field(default_factory=list)  # list[Item] = []

    # exits/directions
    down: str = None
    up: str = None
    north: str = None
    south: str = None
    east: str = None
    west: str = None

    def show(self):
        # room description
        print(self.description)
        print()

        # items in room
        if self.items == []:
            print('Nevidíš tu nič zvláštne.')
        else:
            print('Vidíš:')
            for item in self.items:
                print(f'* {item.name}')

        print()
