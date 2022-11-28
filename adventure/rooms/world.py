from items.coconut_palm_tree import CoconutPalmTree
from items.diamond_on_ceiling import DiamondOnCeiling
from items.empty_seats import EmptySeats
from items.german_car import GermanCar
from items.heavy_chest import HeavyChest
from items.mobile_radiostation import MobileRadiostation
from items.showel import Showel
from items.whip import Whip
from rooms import directions
from .at_enemy_gate import AtEnemyGate
from .free_fall import FreeFall
from .in_plane import InPlane
from .room import Room


def load_world() -> list[Room]:
    return [
        InPlane(
            name='v lietadle',
            description='Prebudil si sa v malom dvojmotorovom lietadle, plachtiacom nad egyptskou púšťou. Je tu '
                        'nádherný kľud, pretože motory stoja a na palube nie je okrem teba živá duša. (Celkom '
                        'zaujímavá situácia, že?) ',
            exits={
                directions.DOWN: 'voľný pád'
            },
            items=[Whip(), EmptySeats()]
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
            description='Si v malej oáze uprostred púšte. Pri malom jazierku stojí palma s niekoľkými kokosovými '
                        'orechmi. Nič moc. Zaujímavejšie je, že kúsok odtiaľto smerom na juh je plot z ostnatého '
                        'drôtu s bránou a strážnou vežou.',
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
            },
            items=[
                GermanCar()
            ]
        ),

        Room(
            name='veliteľov stan',
            description='Si vo veliteľovom stane. Je tu značný neporiadok. Všade dookola je množstvo smetí.',
            exits={
                directions.WEST: 'v tábore',
            },
            items=[
                HeavyChest()
            ]
        ),

        Room(
            name='malý stan',
            description='Si v malom stane. Je tu hromada neužitočných harabúrd.',
            exits={
                directions.EAST: 'v tábore'
            },
            items=[
                Showel(),
                MobileRadiostation()
            ]
        ),

        Room(
            name='podzemie',
            description='Stojíš na kamenných dlaždiciach pod dierou vedúcou von z podzemia. Steny sú pomalované '
                        'výjavmi zo života egyptských bohov.',
            exits={
                directions.UP: 'oáza',
                # directions.EAST: '',
                directions.SOUTH: 'prázdna miestnosť'
            }
        ),

        Room(
            name='prázdna miestnosť',
            description='Stojíš uprostred miestnosti, ktorá je úplne prázdna (jasný príklad toho, že autorovi už '
                        'dochádzajú inšpirácie).',
            exits={
                directions.NORTH: 'podzemie',
                directions.SOUTH: 'komôrka',
                directions.WEST: '',
            }
        ),

        Room(
            name='komôrka',
            description='Si v malej komôrke, ktorej steny sú vyzdobené rozličnými náboženskými motívmi (Bohovia, '
                        'zvieratá, bojovníci, mŕtvoly, atď.).',
            exits={
                directions.NORTH: 'prázdna miestnosť'
            },
            items=[
                DiamondOnCeiling()
            ]
        )
    ]
