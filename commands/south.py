from dataclasses import dataclass
from helpers import show_room
from models import Context
from helpers import get_room_by_name
from world import world


@dataclass(frozen=True)
class South:
    name: str = "juh"
    description: str = "presunieš sa do miestnosti na juh od aktuálnej"

    def exec(self, context: Context, name: str):
        if context.room["exits"]["south"] is None:
            print("Tam sa nedá ísť.")
        else:
            context.room = get_room_by_name(context.room["exits"]["south"], world)
            show_room(context.room)
