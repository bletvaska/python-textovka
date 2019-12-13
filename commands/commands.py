class Commands:
    def __init__(self, commands):
        self._name = 'prikazy'
        self._description = 'Zobrazí zoznam príkazov hry.'
        self._commands = commands

    def exec(self, context):
        print('Zoznam prikazov:')

        for command in self._commands:
            print(f'\t{command._name.upper()} - {command._description}')
