from pydantic import BaseModel
from rich import print


class Room(BaseModel):
    """
    Game room representation.
    """
    name: str
    description: str
    exits: list = []
    items: list = []

    def show(self):
        print(self.description)

        if len(self.items) == 0:
            print('Nevidíš tu nič zvláštne.')
        else:
            print('Vidíš:')
            for item in self.items:
                print(f'* [bold magenta]{item}[/bold magenta]')

        if len(self.exits) == 0:
            print('Z miestnosti nevedú žiadne východy.')
        else:
            print('Možné východy z miestnosti:')
            for exit in self.exits:
                print(f'* [bold yellow]{exit}[/bold yellow]')
