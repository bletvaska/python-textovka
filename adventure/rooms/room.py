from pydantic import BaseModel
from rich import print

from items.item import Item


class Room(BaseModel):
    # fields
    name: str
    description: str
    items: list[Item] = []  # : list
    exits: dict[str, str] = {}

    def act(self, context):
        pass

    def show(self):
        """
        Shows the current room.
        """
        # print description
        print(self.description)

        # print items
        if self.items != []:  # len(current_room.items) > 0
            print('[yellow]Vidíš:[/yellow]')
            for item in self.items:
                print(f'  {item.name}')
        else:
            print('[yellow]Nevidíš tu nič zvláštne.[/yellow]')

        # print exits
        if self.exits == {}:
            print('[magenta]Z tejto miestnosti nevedú žiadne východy.[/magenta]')
        else:
            print('[magenta]Môžeš ísť:[/magenta]')
            for ex in self.exits:
                print(f'  {ex}')
