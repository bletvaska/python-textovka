#!/usr/bin/env python
import world
from commands.about import About
from commands.commands import Commands
from commands.help import Help
from commands.inventory import Inventory
from commands.look_around import LookAround
from commands.quit import Quit
from game_context import GameContext
from helpers import intro, outro, parse_line, get_room_by_name
from room import Room
from states import STATE_PLAYING

intro()

# game initialization
context = GameContext(
    current_room='v lietadle',
    rooms=world.rooms,
    commands=[
        About(),
        Commands(),
        Help(),
        Inventory(),
        LookAround(),
        Quit()
    ]
)

room = get_room_by_name(context.current_room, context.rooms)

# game loop
room.show()

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
