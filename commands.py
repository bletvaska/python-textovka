from pydantic import BaseModel

from rooms import Room
from states import STATE_QUIT, STATE_PLAYING


class Command(BaseModel):
    name: str
    description: str

    def exec(self, current_room: Room):
        raise NotImplementedError('Function exec() was not yet implemented.')


class About(Command):
    name = 'o hre'
    description = 'zobrazí informácie o hre'

    def exec(self, current_room):
        print('Túto mocnú hru spáchal mocný programátor mirek')
        print('(c)2023 by mirek')

        return STATE_PLAYING


class Commands(Command):
    name = 'prikazy'
    description = 'zobrazí zoznam dostupných príkazov v hre'

    def exec(self, current_room):
        print('Zoznam dostupných príkazov v hre:')
        print('* koniec - ukončí hru')
        print('* o hre - zobrazí informácie o hre')
        print('* príkazy - zobrazí zoznam dostupných príkazov v hre')

        return STATE_PLAYING


class Quit(Command):
    name = 'koniec'
    description = 'ukončí hru'

    def exec(self, current_room):
        question = input('Naozaj chceš skončiť? (ano/nie) ').lower().strip()
        if question == 'ano':
            return STATE_QUIT

        return STATE_PLAYING


class LookAround(Command):
    name = 'rozhliadni sa'
    description = 'rozhliadne sa v aktuálnej miestnosti'

    def exec(self, current_room):
        current_room.show()

        return STATE_PLAYING
