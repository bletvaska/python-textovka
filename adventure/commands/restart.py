from helpers import ask_yes_no
from .command import Command


class Restart(Command):
    name: str = 'restart'
    description: str = 'Restarts the adventure'

    def exec(self, context):
        answer = ask_yes_no('Naozaj chceš reštartovať rozohratú hru? ')
        if answer == True:
            context.reset()
            context.current_room.show()


