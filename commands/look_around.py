from game_context import GameContext
from .command import Command


class LookAround(Command):
    def __init__(self):
        super().__init__('rozhliadni sa', 'Vypíše opis miestnosti.')

    def exec(self, context:GameContext):
        context.get_current_room().show()