from items.newspaper import Newspaper
from items.seats import EmptySeats
from rooms.room import Room

world = [
    Room(
        name='v lietadle',
        description='Prebudil si sa v malom dvojmotorovom lietadle, plachtiacom nad egyptskou púšťou. Je tu nádherný '
                    'kľud, pretože motory stoja a na palube nie je okrem teba živá duša. (Celkom zaujímavá situácia, '
                    'že?) ',
        items=[
            Newspaper(),
            EmptySeats()
        ],
        down='vo vzduchu',
    ),

    Room(
        name='vo vzduchu',
        description='Vznášaš sa medzi oblakmi. Uži si tento zaujímavý pocit a vôbec sa nevzrušuj zemou, ktorá sa '
                    'rýchlo približuje. Mimochodom v diaľke na juhu je vidieť nejaký vojenský tábor.',
        down='smrt vo vzduchu'
    ),

    Room(
        name='smrt vo vzduchu',
        description='Vznášaš sa medzi oblakmi. Uži si tento zaujímavý pocit a vôbec sa nevzrušuj zemou, ktorá sa '
                    'rýchlo približuje. Mimochodom v diaľke na juhu je vidieť nejaký vojenský tábor.',
    ),

    Room(
        name='miesto pristatia',
        description='Si na púšti, ktorá sa vyznačuje predovšetkým tým, že je pustá. (Je zaujímavé, že to tu vyzerá '
                    'úplne inak, ako v lietadle).',
        south='oaza'
    ),
    Room(
        name='oaza',
        description='Si v malej oáze uprostred púšte. Pri malom jazierku stojí palma s niekoľkými kokosovými orechmi. '
                    'Nič moc. Zaujímavejšie je, že kúsok odtiaľto smerom na juh je plot z ostnatého drôtu s bránou a '
                    'strážnou vežou.',
        north='miesto pristatia',
        south='pred taborom',
        items=[
            # kokosova palma
        ]
    ),
    Room(
        name='pred taborom',
        description='Stojíš pri plote z ostnatého drôtu. Na juhu je brána, ktorá vedie do vojenského tábora. Na '
                    'blízkej strážnej veži hliadkuje nemecký vojak. Na severe vidíš za piesočnou dunou vrch palmy.',
        north='oaza'
    )

]
