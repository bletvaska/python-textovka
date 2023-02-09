from items.empty_seats import EmptySeats
from items.whip import Whip
from rooms import Room
from rooms.directions import DOWN
from rooms.free_fall import FreeFall
from rooms.in_plane import InPlane


def load_world() -> list[Room]:
    return [
        InPlane(
            name='v lietadle',
            description='Prebudil si sa v malom dvojmotorovom lietadle plachtiacom nad egyptskou púšťou. '
                        'Je tu nádherný kľud, pretože motory sú vypnuté a na palube nie je okrem teba '
                        'živej duše. (Celkom zaujímavá situácia, že áno?)',
            items=[EmptySeats(), Whip()],
            exits={
                DOWN: 'voľný pád'
            }),

        FreeFall(
            name='voľný pád',
            description='Vznášaš sa medzi oblakmi. Uži si tento zaujímavý pocit a vôbec sa nevzrušuj zemou, ktorá sa '
                        'rýchlo približuje. Mimochodom v diaľke na juhu je vidieť nejaký vojenský tábor.',
        ),
    ]
