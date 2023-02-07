import states
from .command import Command


class LookAround(Command):
    name = 'rozhliadni sa'
    description = 'rozhliadne sa v aktuálnej miestnosti'

    def exec(self, room, commands):
        room.show()

        return states.PLAYING
