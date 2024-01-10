from pydantic import BaseModel

import states
from room import Room


class Command(BaseModel):
    """
    Generic command of the game.
    """
    # fields
    name: str
    description: str

    # methods
    def exec(self, room: Room) -> str:
        raise NotImplementedError('This method was not yet implemented.')


class About(Command):
    """
    Shows info about the game.
    """
    name: str = 'o hre'
    description: str = 'zobrazí informácie o hre'

    def exec(self, room):
        print('(c)2024 created by mirek')
        print('Ďalšie dobrodružstvo Indiana Jonesa tentokrát vytvorene v jazyku Python.')

        return states.PLAYING


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


class Quit(Command):
    """
    Quits the game.
    """
    name: str = 'koniec'
    description: str = 'ukončí hru'

    def exec(self, room):
        choice = input('Naozaj chceš skončiť? (a/n) ').lower().strip()
        if choice in ('a', 'y', 'ano', 'yes'):
            print('Ďakujem, že si si zahral túto úžasnú (ukradnutú) hru.')
            return states.QUIT

        return states.PLAYING


class LookAround(Command):
    """
    Look around in the room.
    """
    name: str = 'rozhliadni sa'
    description: str = 'rozhliadne sa v aktuálnej miestnosti'

    def exec(self, room):
        self.show()

        return states.PLAYING
