#!/usr/bin/env python
from commands.about import About
from commands.commands import Commands
from commands.inventory import Inventory
from commands.quit import Quit
from helpers import intro, outro
from states import STATE_PLAYING, STATE_QUIT

intro()
game_state = STATE_PLAYING
backpack = ['revolver', 'bic']
commands = [
    About(),
    Commands(),
    Inventory(),
    Quit()
]

while game_state == STATE_PLAYING:
    line = input('> ').lstrip().rstrip().lower()

    if line == '':  # len(line) == 0
        continue
        # pass

    for command in commands:
        if line == command.name:
            command.exec(backpack, commands)
            break
    else:
        print('Tento príkaz nepoznám.')

outro()
