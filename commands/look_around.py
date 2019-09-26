from game_context import GameContext
from helper import show_room
from .command import Command


class LookAround(Command):
    def __init__(self):
        super().__init__('rozhliadni sa', 'Vypíše opis miestnosti.')

    def exec(self, context:GameContext):
        show_room(context.get_current_room())