from pydantic import BaseModel


class Command(BaseModel):
    """
    Generic command of the game.
    """
    # fields
    name: str
    description: str

    # methods
    def exec(self):
        print("ta vykonavam prikaz ", self.name)


class About(Command):
    """
    Shows info about the game.
    """
    name: str = 'o hre'
    description: str = 'zobrazí informácie o hre'

    def exec(self):
        print('(c)2024 created by mirek')
        print('Dalšie dobrodružstvo Indiana Jonesa tentokrát vytvorene v jazyku Python.')


class Commands(Command):
    """
    Shows all Commmands
    """
    name: str = 'prikazy'
    description: str = 'zobrazí zoznam dostupných príkazov v hre'

    def exec(self):
        print('V hre je možné použiť tieto príkazy:')
        print('* koniec - ukončí rozhratú hru')
        print('* o hre - zobrazí informácie o hre')
        print('* prikazy - zobrazí zoznam dostupných príkazov v hre')
