class GameContext:
    def __init__(self):
        self.backpack = []
        self.world = {}
        self.current_room = None
        self.state = 'playing'