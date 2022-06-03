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
from items.newspaper import Newspaper
from items.revolver import Revolver
from items.whip import Whip

# game init
intro()

context = Context(commands=[
    About(),
    Commands(),
    Examine(),
    Inventory(),
    Quit(),
    Use()
], backpack=[
    Whip(),
    Revolver(),
    Newspaper()
])


while context.game_state == states.PLAYING:
    line = input('> ').lower().lstrip().rstrip()

    if line == '':  # len(line) == 0
        continue

    for command in context.commands:
        if line.startswith(command.name):
            command.exec(context, line)
            break

    else:
        print('Tento príkaz nepoznám.')

outro()
