import states
from commands.command import Command
from rooms.room import Room


class Examine(Command):
    name: str = 'preskumaj'
    description: str = 'zobrazí informácie o zvolenom predmete'

    def exec(self, room: Room) -> str:
        print('zobazujem informacie o predmete')
        return states.PLAYING
