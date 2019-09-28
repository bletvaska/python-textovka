from game_context import GameContext
from .command import Command


class West(Command):
    def __init__(self):
        super().__init__("zapad", "Presunie sa na západ.")
        self.aliases += ['west', 'z', 'w']

    def exec(self, context:GameContext):
        room = context.get_current_room()

        if self.name in room._exits:
            context.current_room = room._exits['zapad']
            context.get_current_room().show()
            context.history.append(self.name)
        else:
            print('tam sa neda ist')