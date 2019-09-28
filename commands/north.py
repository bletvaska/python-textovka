from game_context import GameContext
from .command import Command


class North(Command):
    def __init__(self):
        super().__init__("sever", "Presunie sa na sever.")
        self.aliases += ['north', 's', 'n']

    def exec(self, context:GameContext):
        room = context.get_current_room()

        if self.name in room._exits:
            context.current_room = room._exits['sever']
            context.get_current_room().show()
            context.history.append(self.name)
        else:
            print('tam sa neda ist')
