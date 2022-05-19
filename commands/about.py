from dataclasses import dataclass, field

from commands.command import Command
from context import Context


@dataclass
class About(Command):
    name: str = 'o hre'
    description: str = 'vypíše info o hre'
    aliases: list[str] = field(default_factory=lambda: ['o hre', 'about', 'info', '?'])

    def exec(self, context: Context):
        print('(c)2022 created by mire(c) z koši(c)')
        print('Ďaľšie dobrodružstvo Indiana Jonesa je tentokrát vytvorené v jazyku Python.')
