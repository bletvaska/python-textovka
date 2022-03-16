from dataclasses import dataclass

from .command import Command


@dataclass
class Take(Command):
    name: str = 'vezmi'
    description: str = 'vezme predmet z miestnosti a vloží si ho do batohu'
