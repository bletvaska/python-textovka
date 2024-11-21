from pydantic import BaseModel
from rich import print

import states


class Command(BaseModel):
    """
    Generic game command.
    """
    name: str
    description: str

    def exec(self, backpack: list, commands: list):
        raise NotImplementedError(f'This method was not yet implemented for command {self.name}.')


class About(Command):
    name: str = 'o hre'
    description: str = 'zobrazí informácie o hre'

    def exec(self, backpack, commands):
        print('(c)2024 ukradol mirek')
        print('Ďalšie dobrodružstvo Indiana Jonesa. Tentokrát s jazykom Python.')

        return states.PLAYING


class Quit(Command):
    name: str = "koniec"
    description: str = "ukončí rozohratú hru"

    def exec(self, backpack, commands):
        return states.QUIT


class Commands(Command):
    name: str = "prikazy"
    description: str = "zobrazí zoznam dostupných príkazov v hre"

    def exec(self, backpack, commands: list[Command]):
        print('V hre je možné použiť tieto príkazy:')
        for command in commands:
            print(f'* [bold cyan]{command.name}[/bold cyan] - {command.description}')

        return states.PLAYING


class Inventory(Command):
    name: str = 'inventar'
    description: str = 'zobrazí obsah hráčovho batohu'

    def exec(self, backpack, commands):
        if len(backpack) == 0:  # backpack == []
            print('Batoh je prázdny')
        else:
            print('V batohu máš:')
            for item in backpack:
                print(f'* [bold magenta]{item}[/bold magenta]')

        return states.PLAYING
