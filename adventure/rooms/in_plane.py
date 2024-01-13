from rich import print

from adventure import states
from .room import Room


class InPlane(Room):
    steps: int = 4

    def act(self, context):
        # decrease steps counter
        self.steps -= 1

        # if too many steps, plane crashes
        if self.steps == 0:
            print('Lietadlo šťastne pristálo (strmhlavo). Je mi to ľúto, ale ani taký profesionál ako je Indiana '
                  'Jones nemohol prežiť podobnú radostnú udalosť.')
            context.game_state = states.PLANE_CRASH
