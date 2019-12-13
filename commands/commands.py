from commands.command import Command


class Commands(Command):
    def __init__(self, commands):
        super().__init__('prikazy', 'Zobrazí zoznam príkazov hry.')
        self._commands = commands

    def exec(self, context):
        print('Zoznam prikazov:')

        for command in self._commands:
            print(f'\t{command}')
