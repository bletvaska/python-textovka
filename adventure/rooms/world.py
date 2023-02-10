from items.coconut_palm_tree import CoconutPalmTree
from items.diamond import Diamond
from items.diamond_on_ceiling import DiamondOnCeiling
from items.empty_seats import EmptySeats
from items.german_car import GermanCar
from items.heavy_chest import HeavyChest
from items.mobile_radiostation import MobileRadiostation
from items.shovel import Shovel
from items.whip import Whip
from items.writing_on_wall import WritingOnWall
from rooms import directions
from .altar import Altar
from .at_enemy_gate import AtEnemyGate
from .free_fall import FreeFall
from .in_plane import InPlane
from .room import Room
from .yellow_fog import YellowFog


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
                        'rýchlo približuje. Mimochodom v diaľke na [yellow]juhu[/yellow] je vidieť nejaký vojenský '
                        'tábor.',
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
                        'orechmi. Nič moc. Zaujímavejšie je, že kúsok odtiaľto smerom na [yellow]juh[/yellow] je plot '
                        'z ostnatého drôtu s bránou a strážnou vežou.',
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
            description='Stojíš pri plote z ostnatého drôtu. Na [yellow]juhu[/yellow] je brána, ktorá vedie do '
                        'vojenského tábora. Na blízkej strážnej veži hliadkuje nemecký vojak. Na '
                        '[yellow]severe[/yellow] vidíš za piesočnou dunou vrch palmy.',
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
                Shovel(),
                MobileRadiostation()
            ]
        ),

        Room(
            name='podzemie',
            description='Stojíš na kamenných dlaždiciach pod dierou vedúcou von z podzemia. Steny sú pomalované '
                        'výjavmi zo života egyptských bohov.',
            exits={
                directions.UP: 'oáza',
                directions.EAST: 'uzka chodba',
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
                directions.WEST: 'chodba',
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
        ),

        Room(
            name='chodba',
            description='Stojíš na začiatku širokej chodby, ktorá pokračuje na západ do podivnej žltej hmly. Pri '
                        'stene leží rozpadnutá ľudská kostra, nad ktorou je v stene vyrytý nápis "2Z1S1V".',
            exits={
                directions.EAST: 'prázdna miestnosť',
                directions.WEST: 'žltá hmla'
            }
        ),

        YellowFog(
            name='žltá hmla',
            description='Si v žltej hmle.',
            exits={
                directions.EAST: 'chodba',
                directions.WEST: 'žltá hmla',
                directions.SOUTH: 'žltá hmla',
                directions.NORTH: 'žltá hmla',
            }
        ),

        Room(
            name='koniec chodby',
            description='Si na konci chodby.',
            exits={
                directions.WEST: 'žltá hmla'
            },
            items=[
                Diamond()
            ]
        ),

        Room(
            name='uzka chodba',
            description='Si v úzkej západno-východnej chodbe.',
            items=[
                Diamond(),
                WritingOnWall()
            ],
            exits={
                directions.WEST: 'podzemie',
                directions.EAST: 'oltar'
            }
        ),

        Altar(
            name='oltar',
            description='Stojíš pri veľkom oltári z čistého krištáľu. Z oltára vychádza modré svetlo vrhajúce tiene '
                        'na steny miestnosti. Na [bold yellow]západe[/bold yellow] je vchod do úzkej chodby a na '
                        '[bold yellow]severe[/bold yellow], za závesmi pavučín, vidíš v stene výklenok.',
            exits={
                directions.WEST: 'uzka chodba',
                directions.NORTH: 'vyklenok'
            }
        ),

        Room(
            name='vyklenok',
            description='Si v malom výklenku. Na [bold yellow]juh[/bold yellow] od teba stoji oltár.',
            exits={
                directions.SOUTH: 'oltar'
            },
            items=[
                Diamond()
            ]
        )
    ]
