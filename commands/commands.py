from dataclasses import dataclass
from typing import List

from .command import Command
from context import Context


@dataclass
class Commands(Command):
    name: str = 'prikazy'
    # aliases: List[str]
    description: str = 'vypíše zoznam príkazov hry'

    def exec(self, context: Context, param: str):
        raise NotImplementedError('Command was not yet implemented.')

