from directions import DOWN, UP
from room import Room

rooms = [
    Room(
        name='v lietadle',
        description='Prebudil si sa v malom dvojmotorovom lietadle, plachtiacom nad egyptskou púšťou. Je tu nádherný '
                    'kľud, pretože motory sú vypnuté a na palube nie je okrem teba živá duša. (Celkom zaujímavá '
                    'situácia, že?)',
        exits={
            DOWN: 'vo vzduchu',
            UP: 'do oblakoch'
        },
    ),
    Room(
        name='vo vzduchu',
        description='Vznášaš sa medzi oblakmi. Uži si tento zaujímavý pocit a vôbec sa nevzrušuj zemou, ktorá sa '
                    'rýchlo približuje. Mimochodom v diaľke na juhu je vidieť nejaký vojenský tábor.',
    ),
]
