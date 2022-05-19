from dataclasses import dataclass


@dataclass
class Command:
    name: str
    description: str
    # aliases: list[str]

    def exec(self, context):
        pass
