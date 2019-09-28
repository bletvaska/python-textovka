from game_context import GameContext
from .command import Command


class About(Command):
    def __init__(self):
        super().__init__('o hre', 'Túto hru spáchal mirek v roku 2019. Celkom fajnú.')
        self.aliases += ['about']

    def exec(self, context: GameContext):
        print(self.description)
