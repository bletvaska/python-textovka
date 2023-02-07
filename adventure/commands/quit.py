import states
from commands.command import Command


class Quit(Command):
    name = 'koniec'
    description = 'ukončí rozohratú hru'

    def exec(self, room, commands):
        choice = input('Naozaj chceš ukončiť túto hru? (a/n) ').lower().lstrip().rstrip()
        if choice in ('ano', 'a', 'yes', 'y'):
            return states.QUIT

        return states.PLAYING
