from items.whip import Whip
from . import directions
from .room import Room

rooms = [
    Room(
        name='v lietadle',
        description='Prebudil si sa v malom dvojmotorovom lietadle, plachtiacom nad egyptskou púšťou. Je tu nádherný '
                    'kľud, pretože motory stoja a na palube nie je okrem teba živá duša. (Celkom zaujímavá situácia, '
                    'že?) ',
        exits={
            directions.DOWN: 'vo vzduchu'
        },
        items=[Whip()]
    ),

    Room(
        name='vo vzduchu',
        description='Vznášaš sa medzi oblakmi. Uži si tento zaujímavý pocit a vôbec sa nevzrušuj zemou, ktorá sa '
                    'rýchlo približuje. Mimochodom v diaľke na juhu je vidieť nejaký vojenský tábor.',
        exits={
            directions.DOWN: 'smrt volnym padom'
        }
    ),

    Room(
        name='smrt volnym padom',
        description='Vznášaš sa medzi oblakmi. Uži si tento zaujímavý pocit a vôbec sa nevzrušuj zemou, ktorá sa '
                    'rýchlo približuje. Mimochodom v diaľke na juhu je vidieť nejaký vojenský tábor.',
    ),

    Room(
        name='miesto pristatia',
        description='Si na púšti, ktorá sa vyznačuje predovšetkým tým, že je pustá. (Je zaujímavé, že to tu vyzerá '
                    'úplne inak, ako v lietadle).',
        exits={
            directions.SOUTH: 'oaza'
        }
    ),

    Room(
        name='oaza',
        description='Si v malej oáze uprostred púšte. Pri malom jazierku stojí palma s niekoľkými kokosovými orechmi. '
                    'Nič moc. Zaujímavejšie je, že kúsok odtiaľto smerom na juh je plot z ostnatého drôtu s bránou a '
                    'strážnou vežou.',
        exits={
            directions.NORTH: 'miesto pristatia',
            directions.SOUTH: 'pred taborom',
        },
    ),

    Room(
        name='pred taborom',
        description='Stojíš pri plote z ostnatého drôtu. Na juhu je brána, ktorá vedie do vojenského tábora. Na '
                    'blízkej strážnej veži hliadkuje nemecký vojak. Na severe vidíš za piesočnou dunou vrch palmy.',
        exits={
            directions.NORTH: 'oaza'
        }
    ),

    Room(
        name='uprostred tabora',
        description='Stojíš uprostred vyľudneného vojenského tábora. Na severe je brána vedúca von do púšte. Na '
                    'západe je malý stan, ktorý slúži ako sklad. Na východe je veliteľov stan.',
        exits={
            directions.NORTH: 'pred taborom',
            directions.EAST: 'velitelov stan'
        }
    ),

    Room(
        name='velitelov stan',
        description='Si vo veliteľovom stane. Je tu značný neporiadok. Všade dookola je množstvo smetí.',
        exits={
            directions.WEST: 'uprostred tabora',
        },
    )
]
