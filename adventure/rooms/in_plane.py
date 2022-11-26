import states
from .room import Room


class InPlane(Room):
    steps: int = 0

    def act(self, context, ):
        # increase steps counter
        self.steps += 1

        # if too many steps, plane crashes
        if self.steps > 3:
            print('Lietadlo šťastne pristálo (strmhlavo). Je mi to ľúto, ale ani taký profesionál ako je Indiana '
                  'Jones nemohol prežiť podobnú radostnú udalosť.')
            context.game_state = states.PLANE_CRASH
