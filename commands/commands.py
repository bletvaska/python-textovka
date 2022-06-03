from dataclasses import dataclass

from context import Context
from .command import Command


@dataclass
class Commands(Command):
    name: str = 'prikazy'
    description: str = 'zobrazí zoznam dostupných príkazov v hre'

    def exec(self, context: Context, line: str):
        print('Dostupné príkazy v hre:')
        for command in context.commands:
            print(f'* {command.name} - {command.description}')
