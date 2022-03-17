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

    def show(self):
        """
        Prints description about the room

        Prints out the description about the room given as parameter.
        :param room: room to describe
        """
        print(f'Nachádzaš sa v miestnosti {self.name}')
        print(self.description)

        # print items in the room
        if self.items == []:  # len(room['items'] == 0
            print('Nevidíš tu nič zvláštne.')
        else:
            print("Vidíš:")
            for item in self.items:
                print(f'\t* {item.name}')

        # print exits
        exits = []
        for _exit in self.exits:
            if self.exits[_exit] is not None:
                exits.append(_exit)

        if exits == []:
            print('Z miestnosti nevedú žiadne východy.')
        else:
            print('Môžeš ísť:')
            for ex in exits:
                if ex == Directions.NORTH:
                    print('\t* sever')
                if ex == Directions.SOUTH:
                    print('\t* juh')
                if ex == Directions.EAST:
                    print('\t* východ')
                if ex == Directions.WEST:
                    print('\t* západ')
