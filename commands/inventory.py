from rich import print
from .command import Command


class Inventory(Command):
    name: str = 'inventar'
    description: str = 'zobrazí obsah hráčovho batohu'

    def exec(self, context):
        if len(context.backpack) == 0:
            print('Batoh je prázdny.')
        else:
            print('V batohu máš:')
            for item in context.backpack:
                print(f'* [bold magenta]{item}[/bold magenta]')
