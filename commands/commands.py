from dataclasses import dataclass

from .command import Command


@dataclass
class Commands(Command):
    # fields
    name: str = 'prikazy'
    description: str = 'zobrazí dostupné príkazy v hre'

    # methods
    def exec(self, backpack, commands):
        print('V hre je možné použiť tieto príkazy:')

        for command in commands:
            print(f'* {command.name} - {command.description}')
