from dataclasses import dataclass, field


@dataclass
class About:
    name: str = 'o hre'
    description: str = 'vypíše info o hre'
    # aliases: list[str] = field(default_factory=['o hre', 'about', 'info', '?'])

    def exec(self):
        print('(c)2022 created by mire(c) z koši(c)')
        print('Ďaľšie dobrodružstvo Indiana Jonesa je tentokrát vytvorené v jazyku Python.')
