from rich import print

import states
from rooms.room import Room


class Plane(Room):
    steps: int = 5

    def act(self, context):
        self.steps = self.steps - 1

        if self.steps == 0:
            print('[bold red]Lietadlo šťastne pristálo (strmhlavo). Je mi to ľúto, ale ani taký profesionál ako je Indiana '
                  'Jones nemohol prežiť podobnú radostnú udalosť.[/bold red]')
            context.game_state = states.PLANE_CRASH
