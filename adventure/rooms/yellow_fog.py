from . import directions
from .room import Room

SUCCESS_PATH = 'zapad' 'zapad' 'sever'
#     [
#     'zapad',
#     'zapad',
#     'sever',
#     # 'vychod',
# ]


class YellowFog(Room):
    track: str = ''

    def act(self, context):
        # check if last command was movement command
        cmd = context.history[-1]
        if cmd not in ['sever', 'juh', 'vychod', 'zapad']:
            return

        # evaluate
        self.track += cmd

        if self.track == SUCCESS_PATH:
            self.exits[directions.EAST] = 'koniec chodby'
        elif not SUCCESS_PATH.startswith(self.track):
            self.track = ''
        else:
            self.exits[directions.EAST] = 'chodba'
