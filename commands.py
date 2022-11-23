from dataclasses import dataclass

from states import STATE_QUIT


@dataclass
class Command:
    """
    Describes every command in game.
    """
    # fields
    name: str
    description: str

    # behavior / methods
    def exec(self):
        print('vykonavam prikaz')


@dataclass
class About(Command):
    name: str = 'o hre'
    description: str = 'zobrazí informácie o hre'

    def exec(self):
        print('Hru Indiana Jones 2 napísal mladý nádejný programátor v jazyku Python - mirek v roku 2022.')


@dataclass
class Commands(Command):
    # fields
    name: str = 'prikazy'
    description: str = 'zobrazí dostupné príkazy v hre'

    # methods
    def exec(self):
        print('V hre je možné použiť tieto príkazy:')
        print('* inventar - zobrazi obsah hráčovho batohu')
        print('* koniec - ukončí hru')
        print('* o hre - zobrazi informacie o hre')
        print('* prikazy - zoznam dostupných príkazov v hre')


@dataclass
class Inventory(Command):
    # fields
    name: str = 'inventar'
    description: str = 'zobrazí obsah hráčovho batohu'

    # methods
    def exec(self, backpack: list):
        if len(backpack) == 0:
            print('Batoh je prázdny.')
        else:
            print('V batohu máš:')
            for item in backpack:
                print(item)


@dataclass
class Quit(Command):
    # fields
    name: str = 'koniec'
    description: str = 'ukončí hru'

    # methods
    def exec(self):
        choice = input('Naozaj chceš ukončiť hru? (y/n) ').lstrip().rstrip().lower()
        if choice in ('y', 'yes', 'a', 'ano'):
            game_state = STATE_QUIT
