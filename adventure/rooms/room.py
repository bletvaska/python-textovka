from pydantic import BaseModel
from rich import print


class Room(BaseModel):
    name: str
    description: str
    items: list = []
    exits: list = []

    def show(self):
        # render description
        print(self.description)

        # render items
        if len(self.items) == 0:
            print('Nevidíš tu nič zvláštne.')
        else:
            print('Vidíš: ')
            for item in self.items:
                print(f'* [bold magenta]{item.name}[/bold magenta]')

        # render exits
        if len(self.exits) == 0:
            print('Z miestnosti nevedú žiadne východy.')
        else:
            print('Možné východy z miestnosti: ')
            for ex in self.exits:
                print(f'* [bold yellow]{ex}[/bold yellow]')
