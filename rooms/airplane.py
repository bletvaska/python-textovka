from items.empty_seats import EmptySeats
from items.whip import Whip
from .room import Room


class Airplane(Room):
    name = 'v lietadle'
    description = 'Prebudil si sa v malom dvojmotorovom lietadle plachtiacom nad egyptskou púšťou. Je tu nádherný kľud, pretože motory stoja a na palube nie je okrem teba živej duše. (Celkom zaujímavá situácia, že ano?)'
    items = [
        # Whip(),
        EmptySeats()
    ]
