from rich import print

from commands.command import Command


class Commands(Command):
    """
    Shows all Commmands
    """
    name: str = 'prikazy'
    description: str = 'zobrazí zoznam dostupných príkazov v hre'

    def exec(self, context):
        print('V hre je možné použiť tieto príkazy:')

        for command in context.commands:
            print(f'* [bold cyan]{command.name}[/bold cyan] - {command.description}')
