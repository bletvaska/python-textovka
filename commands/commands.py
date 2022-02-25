from dataclasses import dataclass
from typing import List

from .command import Command
from context import Context


@dataclass
class Commands(Command):
    name: str = 'prikazy'
    # aliases: List[str]
    description: str = 'vypíše zoznam príkazov hry'

    def exec(self, context: Context, param: str):
        print('Zoznam príkazov hry:')

        for command in context.commands:
            # print(f' * {command.name} - {command.description}')
            print(f' * {command}')
