from dataclasses import dataclass
from typing import List

from .command import Command


@dataclass
class About(Command):
    name: str = 'o hre'
    # aliases: List = ['about']
    description: str = 'zobrazí informácie o hre'

    def exec(self, room: dict, backpack: list):
        print('Ďalšie napínavé dobrodružstvo Indiana Jonesa. Tentokrát sa Indy ...')
        print('Túto nadupanú hru spáchal (c) mirek')
