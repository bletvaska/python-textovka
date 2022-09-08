from dataclasses import dataclass

from .command import Command


@dataclass
class Commands(Command):
    name: str = 'prikazy'
    description: str = 'zobrazí zoznam dostupných príkazov v hre'

    def exec(self, context):
        print('V hre je možné použiť tieto príkazy:')

        for command in context.commands:
            print(f'* {command.name} - {command.description}')

        # print('* pouzi - použije zvolený predmet')
