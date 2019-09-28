from game_context import GameContext
from .command import Command


class South(Command):
    def __init__(self):
        super().__init__("juh", "Presunie sa na juh.")
        self.aliases += ['south', 'j']

    def exec(self, context:GameContext):
        room = context.get_current_room()

        if self.name in room._exits:
            context.current_room = room._exits['juh']
            context.get_current_room().show()
            context.history.append(self.name)
        else:
            print('tam sa neda ist')