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
            items=[
                Whip(),
                EmptySeats()
            ]
        ),

        FreeFall(
            name='voľný pád',
            description='Vznášaš sa medzi oblakmi. Uži si tento zaujímavý pocit a vôbec sa nevzrušuj zemou, ktorá sa '
                        'rýchlo približuje. Mimochodom v diaľke na [bold yellow]juhu[/bold yellow] je vidieť nejaký '
                        '[bold green]vojenský tábor[/bold green].',
        ),

        Room(
            name='púšť',
            description='Si na [bold green]púšti[/bold green], ktorá sa vyznačuje predovšetkým tým, že je pustá. (Je '
                        'zaujímavé, že to tu vyzerá úplne inak, ako v lietadle).',
            exits={
                directions.SOUTH: 'oáza',
                directions.NORTH: 'púšť',
                directions.EAST: 'púšť',
                directions.WEST: 'púšť',
            }
        ),

        Room(
            name='oáza',
            description='Si v [bold green]malej oáze[/bold green] uprostred púšte. Pri malom jazierku stojí '
                        '[bold magenta]palma[/bold magenta] s niekoľkými kokosovými orechmi. Nič moc. Zaujímavejšie '
                        'je, že kúsok odtiaľto smerom na [bold yellow]juh[/bold yellow] je plot z ostnatého drôtu s '
                        'bránou a strážnou vežou.',
            exits={
                directions.SOUTH: 'pred táborom',
                directions.NORTH: 'púšť',
                directions.EAST: 'púšť',
                directions.WEST: 'púšť',
            },
            items=[
                CoconutPalmTree()
            ]
        ),

        AtEnemyGate(
            name='pred táborom',
            description='Stojíš [bold green]pri plote[/bold green] z ostnatého drôtu. Na '
                        '[bold yellow]juhu[/bold yellow] je brána, ktorá vedie do '
                        '[bold green]vojenského tábora[/bold green]. Na blízkej strážnej veži hliadkuje nemecký vojak. '
                        'Na [bold yellow]severe[/bold yellow] vidíš za piesočnou dunou vrch '
                        '[bold magenta]palmy[/bold magenta].',
            exits={
                directions.NORTH: 'oáza'
            }
        ),

        Room(
            name='v tábore',
            description='Stojíš uprostred vyľudneného [bold green]vojenského tábora[/bold green]. Na '
                        '[bold yellow]severe[/bold yellow] je brána vedúca von do [bold green]púšte[/bold green]. Na '
                        '[bold yellow]západe[/bold yellow] je [bold green]malý stan[/bold green], ktorý slúži ako '
                        'sklad. Na [bold yellow]východe[/bold yellow] je [bold green]veliteľov stan[/bold green].',
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
            description='Si vo [bold green]veliteľovom stane[/bold green]. Je tu značný neporiadok. Všade dookola je '
                        'množstvo smetí.',
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
            description='Stojíš na kamenných dlaždiciach pod dierou vedúcou von z podzemia. Steny sú pomaľované '
                        'výjavmi zo života egyptských bohov.',
            exits={
                directions.UP: 'oáza',
                directions.EAST: 'úzka chodba',
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
            description='Si v [bold green]malej komôrke[/bold green], ktorej steny sú vyzdobené rozličnými '
                        'náboženskými motívmi (Bohovia, zvieratá, bojovníci, mŕtvoly, atď.).',
            exits={
                directions.NORTH: 'prázdna miestnosť'
            },
            items=[
                DiamondOnCeiling()
            ]
        ),

        Room(
            name='chodba',
            description='Stojíš na začiatku [bold green]širokej chodby[/bold green], ktorá pokračuje na západ do '
                        'podivnej [bold green]žltej hmly[/bold green]. Pri stene leží rozpadnutá ľudská kostra, '
                        'nad ktorou je v stene vyrytý nápis "2Z1S1V".',
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
            name='úzka chodba',
            description='Si v úzkej západno-východnej chodbe.',
            items=[
                Diamond(),
                WritingOnWall()
            ],
            exits={
                directions.WEST: 'podzemie',
                directions.EAST: 'oltár'
            }
        ),

        Altar(
            name='oltár',
            description='Stojíš pri veľkom oltári z čistého krištáľu. Z oltára vychádza modré svetlo vrhajúce tiene '
                        'na steny miestnosti. Na [bold yellow]západe[/bold yellow] je vchod do úzkej chodby a na '
                        '[bold yellow]severe[/bold yellow], za závesmi pavučín, vidíš v stene výklenok.',
            exits={
                directions.WEST: 'úzka chodba',
                directions.NORTH: 'výklenok'
            }
        ),

        Room(
            name='výklenok',
            description='Si v malom výklenku. Na [bold yellow]juh[/bold yellow] od teba stoji oltár.',
            exits={
                directions.SOUTH: 'oltár'
            },
            items=[
                Diamond()
            ]
        )
    ]
