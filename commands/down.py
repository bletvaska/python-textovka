from game_context import GameContext
from helper import show_room
from .command import Command


class Down(Command):
    def __init__(self):
        super().__init__("dolu", "Presunie sa dolu.")

    def exec(self, context:GameContext):
        room = context.get_current_room()

        if self.name in room['exits']:
            context.current_room = room['exits']['dolu']
            show_room(context.get_current_room())
            context.history.append(self.name)
        else:
            print('tam sa neda ist')