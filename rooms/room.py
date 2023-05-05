from rich import print

from pydantic import BaseModel


class Room(BaseModel):
    name: str
    description: str
    items: list = []
    exits: list = []

    def show(self):
        print(self.description)

        print('Vidíš:')
        for item in self.items:
            print(f'  [bold magenta]{item.name}[/bold magenta]')
