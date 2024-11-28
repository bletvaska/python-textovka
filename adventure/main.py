from rich import print

import states
from game_context import GameContext
from helpers import intro, outro, parse_line, get_room_by_name


# game initialization
context = GameContext()
context.current_room = get_room_by_name('v lietadle', context.world)

intro()
context.current_room.show()

# game loop
while context.game_state == states.PLAYING:
    line = input('> ').lower().lstrip().rstrip()

    if line == '':  # len(line) == 0
        continue

    cmd = parse_line(line, context.commands)
    if cmd is None:
        print('Taký príkaz nepoznám.')
    else:
        cmd.exec(context)
        context.current_room.act(context)

outro()
