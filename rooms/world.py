from items.coconut_palm_tree import CoconutPalmTree
from items.empty_seats import EmptySeats
from items.whip import Whip
from . import directions
from .at_enemy_gate import AtEnemyGate
from .free_fall import FreeFall
from .in_plane import InPlane
from .room import Room
rooms = [
    InPlane(
        name='v lietadle',
        description='Prebudil si sa v malom dvojmotorovom lietadle, plachtiacom nad egyptskou púšťou. Je tu nádherný '
                    'kľud, pretože motory stoja a na palube nie je okrem teba živá duša. (Celkom zaujímavá situácia, '
                    'že?) ',
        exits={
            directions.DOWN: 'vo vzduchu'
        },
        items=[Whip(), EmptySeats()]
    ),

    Room(
        name='vo vzduchu',
        description='Vznášaš sa medzi oblakmi. Uži si tento zaujímavý pocit a vôbec sa nevzrušuj zemou, ktorá sa '
                    'rýchlo približuje. Mimochodom v diaľke na juhu je vidieť nejaký vojenský tábor.',
        exits={
            directions.DOWN: 'voľný pád'
        }
    ),

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
            directions.SOUTH: 'oáza',
            directions.NORTH: 'púšť',
            directions.EAST: 'púšť',
            directions.WEST: 'púšť',
        }
    ),

    Room(
        name='oáza',
        description='Si v malej oáze uprostred púšte. Pri malom jazierku stojí palma s niekoľkými kokosovými orechmi. '
                    'Nič moc. Zaujímavejšie je, že kúsok odtiaľto smerom na juh je plot z ostnatého drôtu s bránou a '
                    'strážnou vežou.',
        exits={
            directions.SOUTH: 'pred táborom',
            directions.NORTH: 'púšť',
            directions.EAST: 'púšť',
            directions.WEST: 'púšť',
        },
        items=[CoconutPalmTree()]
    ),

    AtEnemyGate(
        name='pred táborom',
        description='Stojíš pri plote z ostnatého drôtu. Na juhu je brána, ktorá vedie do vojenského tábora. Na '
                    'blízkej strážnej veži hliadkuje nemecký vojak. Na severe vidíš za piesočnou dunou vrch palmy.',
        exits={
            directions.NORTH: 'oáza'
        }
    ),

    Room(
        name='v tábore',
        description='Stojíš uprostred vyľudneného vojenského tábora. Na severe je brána vedúca von do púšte. Na '
                    'západe je malý stan, ktorý slúži ako sklad. Na východe je veliteľov stan.',
        exits={
            directions.NORTH: 'pred táborom',
            directions.EAST: 'veliteľov stan',
            directions.WEST: 'malý stan'
        }
    ),

    Room(
        name='veliteľov stan',
        description='Si vo veliteľovom stane. Je tu značný neporiadok. Všade dookola je množstvo smetí.',
        exits={
            directions.WEST: 'v tábore',
        },
    ),

    Room(
        name='malý stan',
        description='Si v malom stane. Je tu hromada neužitočných harabúrd.',
        exits={
            directions.EAST: 'v tábore'
        }
    )
]

