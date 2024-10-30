import states
from game_context import GameContext
from helpers import intro, outro, parse_line
from rooms.plane import Plane

intro()

# game initialization
context = GameContext()
context.current_room = Plane()

# game loop
context.current_room.show()
while context.game_state == states.PLAYING:
    line = input('> ').lstrip().rstrip().lower()

    if line == '':
        continue

    command, param = parse_line(line, context.commands)
    if command is None:
        print('Taký príkaz nepoznám.')
    else:
        command.exec(context, param)
        context.current_room.act(context)

outro()
