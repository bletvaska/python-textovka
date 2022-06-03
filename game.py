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

    elif line == 'inventar':
        cmd = Inventory()
        cmd.exec(context)

    elif line == 'o hre':
        cmd = About()
        cmd.exec(context)

    elif line.startswith('pouzi'):
        Use().exec(context, line)

    elif line.startswith('preskumaj'):
        Examine().exec(context, line)

    elif line == 'prikazy':
        Commands().exec(context)

    elif line == 'koniec':
        Quit().exec(context)

    else:
        print('Tento príkaz nepoznám.')

outro()
