from game_context import GameContext
from .command import Command


class Quit(Command):
    def __init__(self):
        super().__init__('koniec', 'Ukončí hru.')

    def exec(self, context:GameContext):
        print('ta diky ze si si zahral tuto mocnu hru, lebo je fakt mocna.')
        context.state = 'quit'