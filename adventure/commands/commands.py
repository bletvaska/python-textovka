from rich import print

import states
from .command import Command


class Commands(Command):
    name: str = "prikazy"
    description: str = "zobrazí zoznam dostupných príkazov v hre"

    def exec(self, backpack, commands: list[Command]):
        print('V hre je možné použiť tieto príkazy:')
        for command in commands:
            print(f'* [bold cyan]{command.name}[/bold cyan] - {command.description}')

        return states.PLAYING
