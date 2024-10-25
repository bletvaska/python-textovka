import states
from .command import Command


class Quit(Command):
    name: str = 'koniec'
    description: str = 'ukončí rozohratú hru'

    def exec(self, context):
        choice = input('Naozaj chceš skončiť? (a/n) ').lstrip().rstrip().lower()
        if choice in ['a', 'ano', 'yes', 'ja', 'da']:
            context.game_state = states.QUIT
