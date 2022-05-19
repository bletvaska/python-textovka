from dataclasses import dataclass

from commands.command import Command
from context import Context


@dataclass
class Commands(Command):
    name: str = 'prikazy'
    description: str = 'vypíše zoznam príkazov'

    def exec(self, context: Context):
        print('Zoznam príkazov v hre:')

        for cmd in context.commands:
            print(f'* {cmd.name} - {cmd.description}')
