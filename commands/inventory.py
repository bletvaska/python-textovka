import states
from commands.command import Command
from rooms.room import Room
from rich import print


class Inventory(Command):
    name: str = 'inventar'
    description: str = 'zobrazí obsah hráčovho batohu'

    def exec(self, room: Room, backpack) -> str:
        if backpack == []:
            print("Batoh je prázdny.")
        else:
            print('V batohu máš:')
            for item in backpack:
                print(f'* [bold magenta]{item.name}[/bold magenta]')

        return states.PLAYING
