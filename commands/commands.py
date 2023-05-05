from .command import Command


class Commands(Command):
    name = 'prikazy'
    description = 'zobrazí zoznam dostupných príkazov v hre'

    def exec(self, context):
        print('Zoznam dostupných príkazov v hre:')
        print('* koniec - ukončí hru')
        print('* o hre - zobrazí informácie o hre')
        print('* príkazy - zobrazí zoznam dostupných príkazov v hre')
