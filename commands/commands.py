import states
from commands.command import Command


class Commands(Command):
    """
    Shows all Commmands
    """
    name: str = 'prikazy'
    description: str = 'zobrazí zoznam dostupných príkazov v hre'

    def exec(self, room):
        print('V hre je možné použiť tieto príkazy:')
        print('* koniec - ukončí rozhratú hru')
        print('* o hre - zobrazí informácie o hre')
        print('* prikazy - zobrazí zoznam dostupných príkazov v hre')

        return states.PLAYING
