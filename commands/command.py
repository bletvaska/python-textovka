from dataclasses import dataclass


@dataclass
class Command:
    name: str
    description: str
    # aliases: list

    def exec(self, context):
        raise NotImplementedError('Command execution was not yet implemented.')
