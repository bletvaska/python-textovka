from dataclasses import dataclass

from .command import Command


@dataclass
class About(Command):
    name: str = 'o hre'
    description: str = 'zobrazí informácie o hre'

    def exec(self, context: dict, arg: str):
        print('Indiana Jones a jeho Pythoňácke dobrodružstvo')
        print('Nestarnúci hrdina Indiana Jones sa tentokrát ocitol sám pustý v škaredej miestnosti. A jedine '
              'Pythoňácky programátori mu môžu zachrániť krk. Je to na tebe.\n')
        print('(c) 2021 hru spáchal mirek')
