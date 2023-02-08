import states
from .command import Command


class Quit(Command):
    name = 'koniec'
    description = 'ukončí rozohratú hru'

    def exec(self, context):
        choice = input('Naozaj chceš ukončiť túto hru? (a/n) ').lower().lstrip().rstrip()
        if choice in ('ano', 'a', 'yes', 'y'):
            context.game_state = states.QUIT
