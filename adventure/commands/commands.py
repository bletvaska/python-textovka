import states
from commands.command import Command


class Commands(Command):
    """
    List all the commands of the game.
    """
    name = 'prikazy'
    description = 'zobrazí zoznam dostupných príkazov v hre'

    def exec(self, room, commands: list[Command]):
        print('V hre je možné použiť tieto príkazy:')

        for command in commands:
            print(f'  {command.name} - {command.description}')

        return states.PLAYING
