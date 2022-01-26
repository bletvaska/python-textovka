from dataclasses import dataclass
from helpers import show_room

from models import Context


@dataclass(frozen=True)
class LookAround:
    name: str = "rozhliadni sa"
    description: str = "Vypise popis miestnosti, kde sa prave nachadzas."

    def exec(self, context: Context, name: str):
        show_room(context.room)
