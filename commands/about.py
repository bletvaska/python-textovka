from dataclasses import dataclass, field
from typing import List

from context import Context
from .command import Command


@dataclass
class About(Command):
    name: str = 'o hre'
    # aliases: List[str] = field(default_factory=['about'])
    description: str = 'zobrazí informácie o hre'

    def exec(self, context: Context, param: str):
        print('Ďalšie napínavé dobrodružstvo Indiana Jonesa. Tentokrát sa Indy ...')
        print('Túto nadupanú hru spáchal (c) mirek')
