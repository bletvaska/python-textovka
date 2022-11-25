from dataclasses import dataclass, field

from .directions import DOWN, UP, EAST, WEST, SOUTH, NORTH


@dataclass
class Room:
    name: str
    description: str
    items: list = field(default_factory=list)
    exits: dict = field(default_factory=dict)

    def show(self):
        # room name and description
        print(f'Nachádzaš sa v miestnosti {self.name}.\n')
        print(f'{self.description}\n')

        # items
        if len(self.items) == 0:
            print('Nevidíš tu nič zvláštne.')
        else:
            print('Vidíš:')
            for item in self.items:
                print(f'* {item.name}')

        print()

        # exits
        if len(self.exits) == 0:
            print('Z tejto miestnosti nevedú žiadne východy.')
        else:
            print('Možné východy z miestnosti:')
            if DOWN in self.exits:
                print(f'* dolu')
            if UP in self.exits:
                print(f'* hore')
            if EAST in self.exits:
                print(f'* východ')
            if WEST in self.exits:
                print(f'* západ')
            if SOUTH in self.exits:
                print(f'* juh')
            if NORTH in self.exits:
                print(f'* sever')

        print()
