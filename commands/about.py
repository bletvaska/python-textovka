from dataclasses import dataclass

from helpers import intro
from .command import Command


@dataclass
class About(Command):
    name: str = 'o hre'
    description: str = 'zobrazí informácie o hre'

    def exec(self):
        intro()
        print('Túto megašupabombašpica hru vytvoril v (c)2022 mladý nádejný a atraktívny programátor mirek')
        print('Hra je ďaľším pokračovaním nestarnúceho dobrodruha Indiana Jonesa. Tentokrát je jeho úlohou dostať '
              'sa zo zajatia fašistickej ponorky.')
