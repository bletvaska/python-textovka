from states import STATE_QUIT
from .command import Command


class Quit(Command):
    name = 'koniec'
    description = 'ukončí hru'

    def exec(self, context):
        question = input('Naozaj chceš skončiť? (ano/nie) ').lower().strip()
        if question == 'ano':
            context.game_state = STATE_QUIT
