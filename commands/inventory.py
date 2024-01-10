import states
from commands.command import Command
from rooms.room import Room


class Inventory(Command):
    name: str = 'inventar'
    description: str = 'zobrazí obsah hráčovho batohu'

    def exec(self, room: Room) -> str:
        print('zobrazujem inventar')

        return states.PLAYING
