from game_context import GameContext
from .command import Command


class Commands(Command):
    def __init__(self, commands:list):
        super().__init__('prikazy', 'Zobrazí zoznam príkazov.')
        self._commands = commands

    def exec(self, context:GameContext):
        print('Dostupné príkazy:')
        for command in self._commands:
            print(f'    {command.name}')