import dataclasses


@dataclasses
class Command:
    name: str
    description: str
    aliases: list[str]

    def exec(self):
        pass
