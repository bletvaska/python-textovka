import states
from context import Context
from rooms import Room


class InPlane(Room):
    steps = 3

    def act(self, context: Context):
        # decrease nr of steps
        if self.steps != 0:
            self.steps = self.steps - 1
            return

        # death of indiana jones
        print('Lietadlo šťastne pristálo (strmhlavo). Je mi to ľúto, ale ani taký profesionál ako je Indiana '
              'Jones nemohol prežiť podobnú radostnú udalosť.')

        context.game_state = states.PLANE_CRASH
