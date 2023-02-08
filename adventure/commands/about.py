import states
from .command import Command


class About(Command):
    """
    Shows info about the game.
    """
    name = 'o hre'
    description = 'zobrazí informácie o hre'

    def exec(self, context):
        print('(c)2023 created by mirek')
        print('Dalšie dobrodružstvo Indiana Jonesa je tentokrát vytvorené v jazyku Python.')
