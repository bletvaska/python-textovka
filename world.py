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
        down='vo vzduchu'
    ),

    Room(
        name='vo vzduchu',
        description='Vznášaš sa medzi oblakmi. Uži si tento zaujímavý pocit a vôbec sa nevzrušuj zemou, ktorá sa '
                    'rýchlo približuje. Mimochodom v diaľke na juhu je vidieť nejaký vojenský tábor. '
    )
]
