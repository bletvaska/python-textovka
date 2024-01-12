import states
from rooms.room import Room


class Plane(Room):
    steps: int = 4

    def act(self, context):
        self.steps = self.steps - 1

        if self.steps == 0:
            print('Lietadlo šťastne pristálo (strmhlavo). Je mi to ľúto, ale ani taký profesionál ako je Indiana '
                  'Jones nemohol prežiť podobnú radostnú udalosť.')
            context.game_state = states.PLANE_CRASH
