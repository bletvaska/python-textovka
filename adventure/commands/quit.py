import states
from .command import Command


class Quit(Command):
    name: str = "koniec"
    description: str = "ukončí rozohratú hru"

    def exec(self, backpack, commands):
        return states.QUIT
