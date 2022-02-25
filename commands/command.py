from dataclasses import dataclass


@dataclass
class Command:
    name: str
    # aliases: list
    description: str

    def exec(self, room: dict, backpack: list):
        raise NotImplementedError('Command was not yet implemented.')

    def __str__(self):
        return f'{self.name} - {self.description}'
