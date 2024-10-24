from rich import print

import states
from commands.command import Command


class Commands(Command):
    name: str = 'prikazy'
    description: str = 'zobrazi dostupne prikazy v hre'

    def exec(self, backpack, commands):
        print('V hre je mozne pouzit tieto prikazy:')
        for cmd in commands:
            print(f'* [bold cyan]{cmd.name}[/bold cyan] - {cmd.description}')

        return states.PLAYING






