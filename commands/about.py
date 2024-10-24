import states
from commands.command import Command


class About(Command):
    name: str = 'o hre'
    description: str = 'zobrazí informácie o hre'

    def exec(self, backpack, commands):
        print('(c)2024 created by mirek')
        print('Daľšie dobrodružstvo Indiana Jonesa tentokrát vytvorené v jazyku Python.')
        return states.PLAYING
