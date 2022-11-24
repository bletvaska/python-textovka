#!/usr/bin/env python
from commands.about import About
from commands.commands import Commands
from commands.help import Help
from commands.inventory import Inventory
from commands.quit import Quit
from game_context import GameContext
from helpers import intro, outro, parse_line
from states import STATE_PLAYING

intro()

context = GameContext(
    commands=[
        About(),
        Commands(),
        Help(),
        Inventory(),
        Quit()
    ]
)

while context.game_state == STATE_PLAYING:
    line = input('> ').lstrip().rstrip().lower()

    if line == '':  # len(line) == 0
        continue
        # pass

    command = parse_line(line, context.commands)
    if command is None:
        print('Tento príkaz nepoznám.')
    else:
        command.exec(context, '')



    # for command in context.commands:
    #     if line.startswith(command.name):
    #         param = line.split(command.name, maxsplit=1)[1].lstrip()
    #         command.exec(context, param)
    #         break
    # else:
    #     print('Tento príkaz nepoznám.')

outro()
