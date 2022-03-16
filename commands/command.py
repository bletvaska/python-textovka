from dataclasses import dataclass

from context import Context


@dataclass
class Command:
    name: str
    description: str

    def exec(self, context: Context, arg: str):
        raise NotImplementedError(f'Execution of command "{self.name}" was not yet implemented.')

    def __str__(self):
        return f'{self.name} - {self.description}'
