from dataclasses import dataclass

from models import Context


@dataclass(frozen=True)
class ListOfCommands:
    name: str = "prikazy"
    description: str = "vypíše zoznam príkazov"

    def exec(self, context: Context, name: str):
        print("Zoznam dostupných príkazov:")

        for command in context.commands:
            print(f"  * {command.name} - {command.description}")
