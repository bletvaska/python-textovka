from game_context import GameContext
from .command import Command


class Help(Command):
    def __init__(self, commands:list):
        super().__init__('pomoc', 'Zobrazí pomocníka k jednotlivým príkazom')
        self._commands = commands

    def exec(self, context:GameContext):
        if len(self.params) == 0:
            print('O akom príkaze sa chceš dozvedieť viac?')
            return

        for command in self._commands:
            if command.name == self.params:
                print(command)
                break
        else:
            print('Neznámy príkaz.')