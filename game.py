#!/usr/bin/env python3
import states
from commands.about import About
from commands.commands import Commands
from commands.examine import Examine
from commands.inventory import Inventory
from commands.quit import Quit
from commands.use import Use
from context import Context
from helpers import intro, outro
from items.bucket import Bucket
from items.canister import Canister
from items.door import Door
from items.matches import Matches
from items.newspaper import Newspaper
from items.revolver import Revolver
from items.whip import Whip

intro()

# game init
context = Context()

# list of commands initialization
context.commands = [
    About(),
    Commands(),
    Examine(),
    Inventory(),
    Quit(),
    Use()
]

# backpack initialization
context.backpack = [
    Whip(),
    Revolver(),
    Newspaper(),
    Bucket(),
    Canister(),
    Door(),
    Matches()
]

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

outro()
