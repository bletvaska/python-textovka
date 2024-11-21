from pydantic import BaseModel
from rich import print


class Command(BaseModel):
    """
    Generic game command.
    """
    name: str
    description: str

    def exec(self):
        print(f'vykonavam prikaz {self.name}')


class About(Command):
    name: str = 'o hre'
    description: str = 'zobrazí informácie o hre'

    def exec(self):
        print('(c)2024 ukradol mirek')
        print('Ďalšie dobrodružstvo Indiana Jonesa. Tentokrát s jazykom Python.')


class Quit(Command):
    pass


class Commands(Command):
    name: str = "prikazy"
    description: str = "zobrazí zoznam dostupných príkazov v hre"

    def exec(self):
        print('V hre je možné použiť tieto príkazy:')
        print('* [bold cyan]o hre[/bold cyan] - zobrazí informácie o hre')
        print('* [bold cyan]prikazy[/bold cyan] - zobrazí zoznam dostupných príkazov v hre')
        print('* [bold cyan]koniec[/bold cyan] - ukončí rozohratú hru')
