from rich import print

from .command import Command


class Commands(Command):
    name: str = 'prikazy'
    description: str = 'zobrazi dostupne prikazy v hre'

    def exec(self, context):
        print('V hre je mozne pouzit tieto prikazy:')
        for cmd in context.commands:
            print(f'* [bold cyan]{cmd.name}[/bold cyan] - {cmd.description}')
