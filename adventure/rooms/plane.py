from items.empty_seats import EmptySeats
from items.item import Item
from items.whip import Whip
from .room import Room


class Plane(Room):
    name: str = 'lietadlo'
    description: str = 'Prebudil si sa v [bold green]malom dvojmotorovom lietadle[/bold green] plachtiacom nad egyptskou púšťou. Je ' \
                       'tu nádherný kľud, pretože motory sú vypnuté a na palube nie je okrem teba živej ' \
                       'duše. (Celkom zaujímavá situácia, že áno?)'
    items: list[Item] = [
        Whip(),
        EmptySeats()
    ]
    exits: list = ['dolu']
