from dataclasses import dataclass
from typing import List

from context import Context


@dataclass
class Command:
    name: str
    # aliases: List[str]
    description: str

    def exec(self, context: Context):
        raise NotImplementedError('Command was not yet implemented.')

    def __str__(self):
        return f'{self.name} - {self.description}'
