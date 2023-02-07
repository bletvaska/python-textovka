from pydantic import BaseModel

import states


class Command(BaseModel):
    """
    Generic game command.
    """
    # fields
    name: str
    description: str

    # methods
    def exec(self) -> str:
        raise NotImplementedError('This method was not yet implemented.')


class About(Command):
    """
    Shows info about the game.
    """
    name = 'o hre'
    description = 'zobrazí informácie o hre'

    def exec(self):
        print('(c)2023 created by mirek')
        print('Dalšie dobrodružstvo Indiana Jonesa je tentokrát vytvorené v jazyku Python.')

        return states.PLAYING


class Commands(Command):
    """
    List all the commands of the game.
    """
    name = 'prikazy'
    description = 'zobrazí zoznam dostupných príkazov v hre'

    def exec(self):
        print('V hre je možné použiť tieto príkazy:')
        print('* koniec - ukončí rozohratú hru')
        print('* o hre - zobrazí informácie o hre')
        print('* prikazy - zobrazí zoznam dostupných príkazov v hre')
        print('* rozhliadni sa - rozhliadne sa v aktuálnej miesnosti')

        return states.PLAYING


class Quit(Command):
    name = 'koniec'
    description = 'ukončí rozohratú hru'

    def exec(self):
        choice = input('Naozaj chceš ukončiť túto hru? (a/n) ').lower().lstrip().rstrip()
        if choice in ('ano', 'a', 'yes', 'y'):
            return states.QUIT

        return states.PLAYING


class LookAround(Command):
    name = 'rozhliadni sa'
    description = 'rozhliadne sa v aktuálnej miestnosti'

    def exec(self):
        pass
        # print(current_room.description)
        # if current_room.items != []:  # len(current_room.items) > 0
        #     print('Vidíš:')
        #     for item in current_room.items:
        #         print(f'  {item}')
        # else:
        #     print('Nevidíš tu nič zvláštne.')
