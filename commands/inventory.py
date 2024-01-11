import states
from commands.command import Command
from rich import print


class Inventory(Command):
    name: str = 'inventar'
    description: str = 'zobrazí obsah hráčovho batohu'

    def exec(self, context) -> str:
        if context.backpack == []:
            print("Batoh je prázdny.")
        else:
            print('V batohu máš:')
            for item in context.backpack:
                print(f'* [bold magenta]{item.name}[/bold magenta]')
