import states
from .command import Command


class Commands(Command):
    """
    List all the commands of the game.
    """
    name = 'prikazy'
    description = 'zobrazí zoznam dostupných príkazov v hre'

    def exec(self, context):
        print('V hre je možné použiť tieto príkazy:')

        for command in context.commands:
            print(f'  {command.name} - {command.description}')
