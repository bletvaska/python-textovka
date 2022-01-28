from dataclasses import dataclass
from helpers import show_room
from models import Context
from helpers import get_room_by_name
from world import world


@dataclass(frozen=True)
class West:
    name: str = "zapad"
    description: str = "presunieš sa do miestnosti na západ od aktuálnej"

    def exec(self, context: Context, name: str):
        if context.room["exits"]["west"] is None:
            print("Tam sa nedá ísť.")
        else:
            context.room = get_room_by_name(context.room["exits"]["west"], world)
            show_room(context.room)
