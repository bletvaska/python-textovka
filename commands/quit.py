from dataclasses import dataclass

from models import Context
import states


@dataclass(frozen=True)
class Quit:
    name: str = "koniec"
    description: str = "ukončí rozohratú hru"

    def exec(self, context: Context, name: str):
        line = input("Naozaj chceš skončiť? (a/n) ").lower().lstrip().rstrip()
        if line == "a":
            context.state = states.QUIT
