from commands.command import Command


class West(Command):
    def __init__(self):
        super().__init__('zapad', 'Prejde do miestnosti na západ.')

    def exec(self, context):
        """
            Move to the room on the west.

            If there is an exit to the west from the current room, then current room will change to the room on the west. \
            If the room on the west doesn't exist, then room will not change. And the message will be printed out. On the screen \
             of course.
            :param context: reference to the game context
            :return: nothing
            """

        if 'west' in context.current_room._exits:
            context.current_room = context.current_room._exits['west']
            print(context.current_room)
        else:
            print('tam sa neda ist.')
