from pydantic import BaseModel

import states
from rooms import Room


class Command(BaseModel):
    """
    Generic game command.
    """
    # fields
    name: str
    description: str

    # methods
    def exec(self, room: Room, commands: list) -> str:
        raise NotImplementedError('This method was not yet implemented.')


class About(Command):
    """
    Shows info about the game.
    """
    name = 'o hre'
    description = 'zobrazí informácie o hre'

    def exec(self, room, commands):
        print('(c)2023 created by mirek')
        print('Dalšie dobrodružstvo Indiana Jonesa je tentokrát vytvorené v jazyku Python.')

        return states.PLAYING


class Commands(Command):
    """
    List all the commands of the game.
    """
    name = 'prikazy'
    description = 'zobrazí zoznam dostupných príkazov v hre'

    def exec(self, room, commands):
        print('V hre je možné použiť tieto príkazy:')

        for command in commands:
            print(f'  {command.name} - {command.description}')

        return states.PLAYING


class Quit(Command):
    name = 'koniec'
    description = 'ukončí rozohratú hru'

    def exec(self, room, commands):
        choice = input('Naozaj chceš ukončiť túto hru? (a/n) ').lower().lstrip().rstrip()
        if choice in ('ano', 'a', 'yes', 'y'):
            return states.QUIT

        return states.PLAYING


class LookAround(Command):
    name = 'rozhliadni sa'
    description = 'rozhliadne sa v aktuálnej miestnosti'

    def exec(self, room, commands):
        room.show()

        return states.PLAYING
