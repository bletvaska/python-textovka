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

        # exits from room
        # if self.south is None && self.north is None && ...
        if any([self.north, self.south, self.east, self.west, self.up, self.down]):
            print('Možné východy z miestnosti:')

            if self.north is not None:
                print('* sever')
            if self.south is not None:
                print('* juh')
            if self.east is not None:
                print('* východ')
            if self.west is not None:
                print('* západ')
            if self.down is not None:
                print('* dolu')
            if self.up is not None:
                print('* hore')

        else:
            print('Z tejto miestnosti nevedú žiadne východy.')

        print()
