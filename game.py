#!/usr/bin/env python
from commands.about import About
from commands.commands import Commands
from commands.help import Help
from commands.inventory import Inventory
from commands.look_around import LookAround
from commands.quit import Quit
from game_context import GameContext
from helpers import intro, outro, parse_line
from room import Room
from states import STATE_PLAYING

intro()

# game initialization
context = GameContext(
    commands=[
        About(),
        Commands(),
        Help(),
        Inventory(),
        LookAround(),
        Quit()
    ]
)

room = get_room_by_name('v lietadle', context.rooms)

# game loop
print(room.description)

while context.game_state == STATE_PLAYING:
    line = input('> ').lstrip().rstrip().lower()

    if line == '':  # len(line) == 0
        continue
        # pass

    command = parse_line(line, context.commands)
    if command is None:
        print('Tento príkaz nepoznám.')
    else:
        command.exec(context)

outro()
