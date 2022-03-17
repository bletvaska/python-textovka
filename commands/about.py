from dataclasses import dataclass

from context import Context
from .command import Command


@dataclass
class About(Command):
    name: str = 'o hre'
    description: str = 'zobrazí informácie o hre'

    def __post_init__(self):
        self.aliases += ['about', 'info']

    def exec(self, context: Context, arg: str):
        print('Indiana Jones a jeho Pythoňácke dobrodružstvo')
        print('Nestarnúci hrdina Indiana Jones sa tentokrát ocitol sám pustý v škaredej miestnosti. A jedine '
              'Pythoňácky programátori mu môžu zachrániť krk. Je to na tebe.\n')
        print('(c) 2021 hru spáchal mirek')
