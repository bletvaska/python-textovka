from pydantic import BaseModel
from rich import print

import states


class Command(BaseModel):
    name: str
    description: str

    def exec(self, backpack):
        raise NotImplementedError('This method is not implemented.')


class About(Command):
    name: str = 'o hre'
    description: str = 'zobrazí informácie o hre'

    def exec(self, backpack):
        print('(c)2024 created by mirek')
        print('Daľšie dobrodružstvo Indiana Jonesa tentokrát vytvorené v jazyku Python.')
        return states.PLAYING


class Commands(Command):
    name: str = 'prikazy'
    description: str = 'zobrazi dostupne prikazy v hre'

    def exec(self, backpack, commands):
        print('V hre je mozne pouzit tieto prikazy:')

        # print('* [bold cyan]inventar[/bold cyan] - zobrazi obsah hráčovho batohu')
        # print('* [bold cyan]koniec[/bold cyan] - zobrazi informacie o hre')
        # print('* [bold cyan]o hre[/bold cyan] - zobrazi informacie o hre')
        # print('* [bold cyan]prikazy[/bold cyan] - zobrazi zoznam dostupnych prikazov v hre')
        return states.PLAYING


class Quit(Command):
    name: str = 'koniec'
    description: str = 'ukončí rozohratú hru'

    def exec(self, backpack):
        choice = input('Naozaj chceš skončiť? (a/n) ').lstrip().rstrip().lower()
        if choice in ['a', 'ano', 'yes', 'ja', 'da']:
            return states.QUIT

        return states.PLAYING

class Inventory(Command):
    name: str = 'inventar'
    description: str = 'zobrazí obsah hráčovho batohu'

    def exec(self, backpack):
        if len(backpack) == 0:
            print('Batoh je prázdny.')
        else:
            print('V batohu máš:')
            for item in backpack:
                print(f'* [bold magenta]{item}[/bold magenta]')

        return states.PLAYING
