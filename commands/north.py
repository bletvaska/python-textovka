from dataclasses import dataclass
from helpers import show_room
from models import Context
from helpers import get_room_by_name
from world import world


@dataclass(frozen=True)
class North:
    name: str = "sever"
    description: str = "presunieš sa do miestnosti na sever od aktuálnej"

    def exec(self, context: Context, name: str):
        if context.room["exits"]["north"] is None:
            print("Tam sa nedá ísť.")
        else:
            context.room = get_room_by_name(context.room["exits"]["north"], world)
            show_room(context.room)

            # save command to history
            context.history.append('sever')
