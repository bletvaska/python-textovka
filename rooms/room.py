from rich import print
from pydantic import BaseModel


class Room(BaseModel):
    name: str
    description: str
    items: list = []
    exits: dict = {}

    def act(self, context):
        pass

    def show(self):
        print(self.description)

        if len(self.items) == 0:
            print('Nevidíš tu nič zaujímavé.')
        else:
            print('Vidíš:')
            for item in self.items:
                print(f'  [bold magenta]{item.name}[/bold magenta]')
