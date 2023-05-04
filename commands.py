from pydantic import BaseModel

from game_context import GameContext
from states import STATE_QUIT


class Command(BaseModel):
    name: str
    description: str

    def exec(self, context: GameContext):
        raise NotImplementedError('Function exec() was not yet implemented.')


class About(Command):
    name = 'o hre'
    description = 'zobrazí informácie o hre'

    def exec(self, context):
        print('Túto mocnú hru spáchal mocný programátor mirek')
        print('(c)2023 by mirek')


class Commands(Command):
    name = 'prikazy'
    description = 'zobrazí zoznam dostupných príkazov v hre'

    def exec(self, context):
        print('Zoznam dostupných príkazov v hre:')
        print('* koniec - ukončí hru')
        print('* o hre - zobrazí informácie o hre')
        print('* príkazy - zobrazí zoznam dostupných príkazov v hre')


class Quit(Command):
    name = 'koniec'
    description = 'ukončí hru'

    def exec(self, context):
        question = input('Naozaj chceš skončiť? (ano/nie) ').lower().strip()
        if question == 'ano':
            context.game_state = STATE_QUIT


class LookAround(Command):
    name = 'rozhliadni sa'
    description = 'rozhliadne sa v aktuálnej miestnosti'

    def exec(self, context):
        context.current_room.show()
