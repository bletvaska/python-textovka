import states
from commands.command import Command


class Quit(Command):
    name: str = 'koniec'
    description: str = 'ukončí rozohratú hru'

    def exec(self, backpack, commands):
        choice = input('Naozaj chceš skončiť? (a/n) ').lstrip().rstrip().lower()
        if choice in ['a', 'ano', 'yes', 'ja', 'da']:
            return states.QUIT

        return states.PLAYING
