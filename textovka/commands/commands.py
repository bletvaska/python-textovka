from rich import print

from .command import Command


class Commands(Command):
    name = 'prikazy'
    description = 'zobrazí zoznam dostupných príkazov v hre'

    def exec(self, context):
        print('Zoznam dostupných príkazov v hre:')

        # list all available commands
        for command in context.commands:
            print(f'* [bold cyan]{command.name:13}[/bold cyan] - {command.description}')
