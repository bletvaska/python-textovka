from dataclasses import dataclass


@dataclass
class Command:
    name: str
    description: str

    def exec(self, context: dict, arg: str):
        raise NotImplementedError(f'Execution of command "{self.name}" was not yet implemented.')

    def __str__(self):
        return f'{self.name} - {self.description}'
