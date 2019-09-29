from game_context import GameContext
from .command import Command


class Down(Command):
    def __init__(self):
        super().__init__("dolu", "Presunie sa dolu.")
        self.aliases += ['down', 'd']

    def exec(self, context:GameContext):
        room = context.get_current_room()

        if self.name in room._exits:
            context.current_room = room._exits['dolu']
            context.get_current_room().show()
            context.history.append(self.name)
        else:
            print('Tam sa nedá ísť.')