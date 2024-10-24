from pydantic import BaseModel

import states


class Command(BaseModel):
    name: str
    description: str

    def exec(self):
        raise NotImplementedError('This method is not implemented.')


class About(Command):
    name: str = 'o hre'
    description: str = 'zobrazí informácie o hre'

    def exec(self):
        print('(c)2024 created by mirek')
        print('Daľšie dobrodružstvo Indiana Jonesa tentokrát vytvorené v jazyku Python.')
        return states.PLAYING


class Commands(Command):
    name: str = 'prikazy'
    description: str = 'zobrazi dostupne prikazy v hre'

    def exec(self):
        print('V hre je mozne pouzit tieto prikazy:')
        print('* koniec - zobrazi informacie o hre')
        print('* o hre - zobrazi informacie o hre')
        print('* prikazy - zobrazi zoznam dostupnych prikazov v hre')
        return states.PLAYING


class Quit(Command):
    name: str = 'koniec'
    description: str = 'ukončí rozohratú hru'

    def exec(self):
        choice = input('Naozaj chceš skončiť? (a/n) ').lstrip().rstrip().lower()
        if choice in ['a', 'ano', 'yes', 'ja', 'da']:
            return states.QUIT

        return states.PLAYING
