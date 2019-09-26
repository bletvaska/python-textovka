class GameContext:
    def __init__(self):
        self.backpack = []
        self.world = {}
        self.current_room = None
        self.state = 'playing'
        self.history = []

    def get_current_room(self):
        return self.world[self.current_room]
