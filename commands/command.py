from dataclasses import dataclass


@dataclass
class Command:
    name: str
    description: str
    # aliases: list[str]

    def exec(self, context):
        raise NotImplementedError('Execution of the command was not yet implemented.')
