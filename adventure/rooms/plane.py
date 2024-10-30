import states
from items.empty_seats import EmptySeats
from items.item import Item
from items.whip import Whip
from .direction import DOWN
from .room import Room


class Plane(Room):
    name: str = 'lietadlo'
    description: str = 'Prebudil si sa v [bold green]malom dvojmotorovom lietadle[/bold green] plachtiacom nad ' \
                       'egyptskou púšťou. Je tu nádherný kľud, pretože motory sú vypnuté a na palube nie je okrem ' \
                       'teba živej duše. (Celkom zaujímavá situácia, že áno?)'
    items: list[Item] = [
        Whip(),
        EmptySeats()
    ]
    exits: dict = {
        DOWN: 'voľný pád'
    }
    steps: int = 4

    def act(self, context):
        self.steps = self.steps - 1

        if self.steps == 0:
            print('Lietadlo šťastne pristálo (strmhlavo). Je mi to ľúto, ale ani taký profesionál ako je Indiana Jones nemohol prežiť podobnú radostnú udalosť.')
            context.game_state = states.PLANE_CRASH
