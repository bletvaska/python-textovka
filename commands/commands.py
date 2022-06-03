from dataclasses import dataclass

from .command import Command


@dataclass
class Commands(Command):
    name: str = 'prikazy'
    description: str = 'zobrazí zoznam dostupných príkazov v hre'

    def exec(self):
        print('Dostupné príkazy v hre:')
        print('* inventar - zobrazí obsah hráčovho batohu')
        print('* koniec - ukončí rozohratú hru')
        print('* o hre - zobrazí informácie o hre')
        print('* pouzi - použije zvolený predmet')
        print('* preskumaj - zobrazí opis zvoleného predmetu')
        print('* prikazy - zobrazí zoznam dostupných príkazov v hre')
