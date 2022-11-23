from dataclasses import dataclass

from .command import Command


@dataclass
class Help(Command):
    name: str = 'pomoc'
    description: str = 'zobrazí pomocníka ku zvolenému príkazu'

    def exec(self, context, param):
        print('zatial sa ti dari dost dobre')
