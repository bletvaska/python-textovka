from dataclasses import dataclass

from .command import Command


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
