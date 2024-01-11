import states
from commands.command import Command


class LookAround(Command):
    """
    Look around in the room.
    """
    name: str = 'rozhliadni sa'
    description: str = 'rozhliadne sa v aktuálnej miestnosti'

    def exec(self, context):
        context.current_room.show()
