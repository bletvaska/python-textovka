from rich import print
from .command import Command


class Inventory(Command):
    name = 'inventar'
    description = 'zobrazí obsah batohu'

    def exec(self, context):
        # is backpack empty?
        # if context.backpack == []:
        if len(context.backpack) == 0:
            print('Batoh je prázdny.')

        # something in backpack
        else:
            print('V batohu máš:')
            for item in context.backpack:
                print(f'  [bold magenta]{item.name}[/bold magenta]')
