from game_context import GameContext
from .command import Command


class Load(Command):
    def __init__(self):
        super().__init__('nacitaj', 'Nahrá uloženú pozíciu s disku')

    def exec(self, context: GameContext):
        pass