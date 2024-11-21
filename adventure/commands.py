from pydantic import BaseModel
from rich import print

import states


class Command(BaseModel):
    """
    Generic game command.
    """
    name: str
    description: str

    def exec(self):
        raise NotImplementedError(f'This method was not yet implemented for command {self.name}.')


class About(Command):
    name: str = 'o hre'
    description: str = 'zobrazí informácie o hre'

    def exec(self):
        print('(c)2024 ukradol mirek')
        print('Ďalšie dobrodružstvo Indiana Jonesa. Tentokrát s jazykom Python.')

        # return None


class Quit(Command):
    name: str = "koniec"
    description: str = "ukončí rozohratú hru"

    def exec(self):
        return states.QUIT


class Commands(Command):
    name: str = "prikazy"
    description: str = "zobrazí zoznam dostupných príkazov v hre"

    def exec(self):
        print('V hre je možné použiť tieto príkazy:')
        print('* [bold cyan]inventar[/bold cyan] - zobrazí obsah hráčovho batohu')
        print('* [bold cyan]o hre[/bold cyan] - zobrazí informácie o hre')
        print('* [bold cyan]koniec[/bold cyan] - ukončí rozohratú hru')
        print('* [bold cyan]prikazy[/bold cyan] - zobrazí zoznam dostupných príkazov v hre')


class Inventory(Command):
    name: str = 'inventar'
    description: str = 'zobrazí obsah hráčovho batohu'

    def exec(self, backpack):
        if len(backpack) == 0:
            print('Batoh je prázdny')
        else:
            print('V batohu máš:')
            for item in backpack:
                print(item)
