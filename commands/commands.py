from dataclasses import dataclass

from .command import Command


@dataclass
class Commands(Command):
    name: str = 'prikazy'
    description: str = 'zobrazí zoznam dostupných príkazov v hre'

    def exec(self, context):
        print('V hre je možné použiť tieto príkazy:')
        print('* inventar - zobrazí obsah batohu')
        print('* koniec - ukončí rozohratú hru')
        print('* o hre - zobrazí informácie o hre')
        print('* pouzi - použije zvolený predmet')
        print('* preskumaj - preskúma zvolený predmet')
        print('* prikazy - zobrazí zoznam dostupných príkazov v hre')
