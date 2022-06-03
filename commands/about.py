from dataclasses import dataclass

from context import Context
from .command import Command
# from commands.command import Command


@dataclass
class About(Command):
    name: str = 'o hre'
    description: str = 'zobrazí informácie o hre'

    def exec(self, context: Context, line: str):
        print('(c)2022 created by mighty mire(c) the programmer')
        print('Ďalšie dobrodružstvo Indiana Jonesa. Tentokrát je jeho úlohou uniknúť z podzmeného väzenia, '
              'v ktorom sa náhodou ocitol.')
