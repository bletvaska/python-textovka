from dataclasses import dataclass

from context import Context
from .command import Command


@dataclass
class Commands(Command):
    name: str = 'prikazy'
    description: str = 'vypíše zoznam príkazov v hre'

    def __post_init__(self):
        self.aliases += ['commands', 'help']

    def exec(self, context: Context, arg: str):
        print('Zoznam príkazov:')

        for cmd in context.commands:
            print(f'  {cmd}')
