from dataclasses import dataclass

from items.item import Item


@dataclass
class Room:
    name: str
    description: str
    items: list[Item]
    exits: list[str]

    def show(self):
        print(f'Nachádzaš sa v miestnosti {self.name}.')
        print(self.description)

        # show items
        if len(self.items) == 0:
            print('Nevídiš tu nič zvláštne.')
        else:
            print('Vidíš: ')
            # print(', '.join(self.items))
            for item in self.items:
                print(f'  {item.name}')

        # show exits
        if len(self.exits) == 0:
            print('Z miestnosti nevedú žiadne východy.')
        else:
            print('Východy z miestnosti:')
            for ext in self.exits:
                print(f'  {ext}')
