import states
from commands.command import Command
from rooms.room import Room


class Inventory(Command):
    name: str = 'inventar'
    description: str = 'zobrazí obsah hráčovho batohu'

    def exec(self, room: Room, backpack) -> str:
        print('zobrazujem inventar')
        print(backpack)

        return states.PLAYING
