from rich import print

from .command import Command


class Commands(Command):
    name: str = "prikazy"
    description: str = "zobrazí zoznam dostupných príkazov v hre"

    def exec(self, context):
        print('V hre je možné použiť tieto príkazy:')
        for command in context.commands:
            print(f'* [bold cyan]{command.name}[/bold cyan] - {command.description}')
