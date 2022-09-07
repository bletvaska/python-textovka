from dataclasses import dataclass


@dataclass
class Command:
    name: str
    description: str
    parameter: str = None

    def exec(self):
        raise NotImplementedError('This command has not execution part.')
