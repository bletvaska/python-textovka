#!/usr/bin/env python
from commands.drop import Drop
from commands.examine import Examine
from commands.take import Take
from commands.use import Use
from items.whip import Whip
from rooms import world
from commands.about import About
from commands.commands import Commands
from commands.down import Down
from commands.east import East
from commands.help import Help
from commands.inventory import Inventory
from commands.look_around import LookAround
from commands.north import North
from commands.quit import Quit
from commands.south import South
from commands.up import Up
from commands.west import West
from game_context import GameContext
from helpers import intro, outro, parse_line, get_room_by_name, get_item_by_name
from states import STATE_PLAYING, DEATH_BY_FREE_FALL, SHOT_BY_ENEMY

intro()

# game initialization
context = GameContext(
    current_room='v lietadle',
    rooms=world.rooms,
    commands=[
        About(),
        Commands(),
        Down(),
        Drop(),
        East(),
        Examine(),
        Help(),
        Inventory(),
        LookAround(),
        North(),
        Quit(),
        South(),
        Take(),
        Up(),
        Use(),
        West()
    ],
)

room = get_room_by_name(context.current_room, context.rooms)

room.show(context)

# game loop
while context.game_state == STATE_PLAYING:
    line = input('> ').lstrip().rstrip().lower()

    if line == '':  # len(line) == 0
        continue
        # pass

    # parse command line
    command = parse_line(line, context.commands)
    if command is None:
        print('Tento príkaz nepoznám.')
    else:
        command.exec(context)

    # check game state
    if context.current_room == 'smrt volnym padom':
        context.game_state = DEATH_BY_FREE_FALL

if context.game_state == DEATH_BY_FREE_FALL:
    print('Ta si spadol a zabil sa bez padaka')

outro()
