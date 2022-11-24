#!/usr/bin/env python
from commands.about import About
from commands.commands import Commands
from commands.help import Help
from commands.inventory import Inventory
from commands.quit import Quit
from game_context import GameContext
from helpers import intro, outro, parse_line
from room import Room
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

room = Room(
    name='v lietadle',
    description='Prebudil si sa v malom dvojmotorovom lietadle, plachtiacom nad egyptskou púšťou. Je tu nádherný '
                'kľud, pretože motory sú vypnuté a na palube nie je okrem teba živá duša. (Celkom zaujímavá situácia, '
                'že?)'
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
        command.exec(context)

outro()
