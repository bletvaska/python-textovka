from game_context import GameContext
from helper import show_room
from .command import Command


class East(Command):
    def __init__(self):
        super().__init__("vychod", "Presunie sa na vychod.")
        self.aliases += ['east', 'v', 'e']

    def exec(self, context:GameContext):
        """
        Enter the room on east from current room.
        If there is no exit to the east, then no change. The new room will be returned from the function.
        :param world: the world the player is in
        :param current_room: the name of current room player is in
        :return: the name of new room on the east
        """
        room = context.get_current_room()

        if self.name in room['exits']:
            context.current_room = room['exits']['vychod']
            show_room(context.get_current_room())
            context.history.append(self.name)
        else:
            print('tam sa neda ist')