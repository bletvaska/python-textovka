import states
from items.empty_seats import EmptySeats
from items.whip import Whip
from rooms.room import Room


class Plane(Room):
    name: str = 'v lietadle'
    description: str = 'Prebudil si sa v malom dvojmotorovom lietadle plachtiacom nad egyptskou púšťou. Je tu nádherný kľud, pretože motory sú vypnuté a na palube nie je okrem teba živej duše. (Celkom zaujímavá situácia, že áno?)'
    items: list = [Whip(), EmptySeats()]
    steps: int = 3

    def act(self, context):
        self.steps = self.steps - 1

        if self.steps == 0:
            print('Lietadlo šťastne pristálo (strmhlavo). Je mi to ľúto, ale ani taký profesionál ako je Indiana '
                  'Jones nemohol prežiť podobnú radostnú udalosť.')
            context.game_state = states.PLANE_CRASH
