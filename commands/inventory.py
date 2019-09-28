from game_context import GameContext
from .command import Command


class Inventory(Command):
    def __init__(self):
        super().__init__('inventar', 'Zobrazí obsah batohu.')
        self.aliases += ['batoh', 'i']

    def exec(self, context:GameContext):
        if len(context.backpack) > 0:
            print('V batohu máš:')
            for item in context.backpack:
                print(f'     {item.name}')
        else:
            print('Batoh je prázdny.')