from items.coconut_palm_tree import CoconutPalmTree
from items.empty_seats import EmptySeats
from items.whip import Whip
from rooms import Room
from rooms.directions import DOWN, SOUTH, NORTH, WEST, EAST
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

        Room(
            name='púšť',
            description='Si na púšti, ktorá sa vyznačuje predovšetkým tým, že je pustá. (Je zaujímavé, že to tu vyzerá '
                        'úplne inak, ako v lietadle).',
            exits={
                SOUTH: 'oáza',
                NORTH: 'púšť',
                WEST: 'púšť',
                EAST: 'púšť'
            }
        ),

        Room(
            name='oáza',
            description='Si v malej oáze uprostred púšte. Pri malom jazierku stojí palma s niekoľkými kokosovými '
                        'orechmi. Nič moc. Zaujímavejšie je, že kúsok odtiaľto smerom na juh je plot z ostnatého '
                        'drôtu s bránou a strážnou vežou.',
            exits={
                SOUTH: 'pred táborom',
                NORTH: 'púšť',
                EAST: 'púšť',
                WEST: 'púšť',
            },
            items=[CoconutPalmTree()]
        ),


    ]
