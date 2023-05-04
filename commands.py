from pydantic import BaseModel

from states import STATE_QUIT, STATE_PLAYING


class Command(BaseModel):
    name: str
    description: str

    def exec(self):
        print('>>> chyba implementacia metody exec')


class About(Command):
    name = 'o hre'
    description = 'zobrazí informácie o hre'

    def exec(self):
        print('Túto mocnú hru spáchal mocný programátor mirek')
        print('(c)2023 by mirek')


class Commands(Command):
    name = 'prikazy'
    description = 'zobrazí zoznam dostupných príkazov v hre'

    def exec(self):
        print('Zoznam dostupných príkazov v hre:')
        print('* koniec - ukončí hru')
        print('* o hre - zobrazí informácie o hre')
        print('* príkazy - zobrazí zoznam dostupných príkazov v hre')


class Quit(Command):
    name = 'koniec'
    description = 'ukončí hru'

    def exec(self):
        question = input('Naozaj chceš skončiť? (ano/nie) ').lower().strip()
        if question == 'ano':
            return STATE_QUIT

        return STATE_PLAYING
