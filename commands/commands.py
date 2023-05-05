from .command import Command


class Commands(Command):
    name = 'prikazy'
    description = 'zobrazí zoznam dostupných príkazov v hre'

    def exec(self, context):
        print('Zoznam dostupných príkazov v hre:')
