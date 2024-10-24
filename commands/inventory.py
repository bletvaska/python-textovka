from rich import print
import states
from .command import Command


class Inventory(Command):
    name: str = 'inventar'
    description: str = 'zobrazí obsah hráčovho batohu'

    def exec(self, backpack, commands):
        if len(backpack) == 0:
            print('Batoh je prázdny.')
        else:
            print('V batohu máš:')
            for item in backpack:
                print(f'* [bold magenta]{item}[/bold magenta]')

        return states.PLAYING
