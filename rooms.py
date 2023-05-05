from pydantic import BaseModel
from rich import print

from items import Whip, EmptySeats


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


class Airplane(Room):
    name = 'v lietadle'
    description = 'Prebudil si sa v malom dvojmotorovom lietadle plachtiacom nad egyptskou púšťou. Je tu nádherný kľud, pretože motory stoja a na palube nie je okrem teba živej duše. (Celkom zaujímavá situácia, že ano?)'
    items = [
        Whip(),
        EmptySeats()
    ]
