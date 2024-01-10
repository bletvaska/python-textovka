import states
from commands.command import Command


class About(Command):
    """
    Shows info about the game.
    """
    name: str = 'o hre'
    description: str = 'zobrazí informácie o hre'

    def exec(self, room, backpack):
        print('(c)2024 created by mirek')
        print('Ďalšie dobrodružstvo Indiana Jonesa tentokrát vytvorene v jazyku Python.')

        return states.PLAYING
