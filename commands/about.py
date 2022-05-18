from dataclasses import dataclass, field

from context import Context


@dataclass
class About:
    name: str = 'o hre'
    description: str = 'vypíše info o hre'
    aliases: list[str] = field(default_factory=lambda: ['o hre', 'about', 'info', '?'])

    def exec(self, line: str, context: Context):
        print('(c)2022 created by mire(c) z koši(c)')
        print('Ďaľšie dobrodružstvo Indiana Jonesa je tentokrát vytvorené v jazyku Python.')
