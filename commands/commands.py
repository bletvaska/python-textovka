from dataclasses import dataclass

from .command import Command


@dataclass
class Commands(Command):
    name: str = 'prikazy'
    description: str = 'vypíše zoznam príkazov v hre'

    def exec(self, context: dict, arg: str):
        print('Zoznam príkazov:')

        for cmd in context['commands']:
            print(cmd)
