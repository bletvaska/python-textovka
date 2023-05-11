import states
from items.empty_seats import EmptySeats
from items.whip import Whip
from . import directions
from .room import Room


class Airplane(Room):
    name = 'v lietadle'
    description = 'Prebudil si sa v malom dvojmotorovom lietadle plachtiacom nad egyptskou púšťou. Je tu nádherný kľud, pretože motory stoja a na palube nie je okrem teba živej duše. (Celkom zaujímavá situácia, že ano?)'
    items = [
        Whip(),
        EmptySeats()
    ]
    exits = {
        directions.DOWN: 'voľný pád',
    }
    counter = 0

    def act(self, context):
        self.counter = self.counter + 1

        if self.counter == 4:
            print(
                'Lietadla šťastne pristálo (strmhlav). Je mi to ľúto, ale ani taký profesionál, ako je Indiana Jones nemohol prežiť podobnú radostnú udalosť.')
            context.game_state = states.STATE_DEATH
