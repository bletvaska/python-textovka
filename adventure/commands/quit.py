import states
from helpers import ask_yes_no
from .command import Command


class Quit(Command):
    name: str = "koniec"
    description: str = "ukončí rozohratú hru"

    def exec(self, context):
        answer = ask_yes_no('Chceš skončiť hru? (a/n)')
        if answer == True:
            context.game_state = states.QUIT
