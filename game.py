#!/usr/bin/env python3
import states
from commands.about import About
from commands.commands import Commands
from commands.drop import Drop
from commands.east import East
from commands.examine import Examine
from commands.inventory import Inventory
from commands.lookaround import LookAround
from commands.quit import Quit
from commands.take import Take
from commands.use import Use
from context import Context
from helpers import intro, outro, congratulations, get_room_by_name
from items.newspaper import Newspaper
from world import world

intro()

# create context
context = Context(
    world=world,
    current_room=get_room_by_name('dungeon', world)
)

# list of commands initialization
context.commands = [
    About(),
    Commands(),
    Drop(),
    East(),
    Examine(),
    Inventory(),
    LookAround(),
    Quit(),
    Take(),
    Use()
]

# backpack initialization
context.backpack = [
    Newspaper(),
]

context.current_room.show()

# main loop
while context.game_state == states.PLAYING:
    line = input('> ').lower().lstrip().rstrip()

    if line == '':  # len(line) == 0
        continue

    for command in context.commands:
        if line.startswith(command.name):
            name = line.split(command.name)[1].lstrip()
            command.exec(context, name)
            break

    else:
        print('Tento príkaz nepoznám.')

if context.game_state == states.WINNER:
    congratulations()

outro()
