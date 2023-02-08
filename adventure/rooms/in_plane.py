from rooms import Room


class InPlane(Room):
    steps = 0

    def act(self, context):
        print('acting now')
