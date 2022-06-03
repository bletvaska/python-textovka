from dataclasses import dataclass

from context import Context


@dataclass
class Command:
    name: str
    description: str
    # aliases: list

    def exec(self, context: Context):
        raise NotImplementedError('Command execution was not yet implemented.')
