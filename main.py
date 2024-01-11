#!/usr/bin/env python3
import states
from commands.about import About
from commands.commands import Commands
from commands.drop import Drop
from commands.examine import Examine
from commands.inventory import Inventory
from commands.look_around import LookAround
from commands.quit import Quit
from commands.take import Take
from game_context import GameContext
from helpers import intro, outro, parse_line
from items.empty_seats import EmptySeats
from items.whip import Whip
from rooms.room import Room

# game initialization
context = GameContext(
    commands=[
        About(),
        Commands(),
        Drop(),
        Examine(),
        Inventory(),
        LookAround(),
        Quit(),
        Take(),
    ],
    current_room=Room(
        name='v lietadle',
        description='Prebudil si sa v malom dvojmotorovom lietadle plachtiacom nad egyptskou púšťou. Je '
                    'tu nádherný kľud, pretože motory sú vypnuté a na palube nie je okrem teba živej '
                    'duše. (Celkom zaujímavá situácia, že áno?)',
        items=[Whip(), EmptySeats()],
        # exits=[]
    )
)
context.commands.sort()

# game loop
intro()
context.current_room.show()
print()

while context.game_state == states.PLAYING:
    line = input('> ').lower().lstrip().rstrip()  # echo line | lower | lstrip | rstrip

    # is line empty?
    if line == '':  # if len(line) == 0:
        continue  # {}

    # parse and execute command
    command = parse_line(line, context.commands)
    if command is None:
        print('Taký príkaz nepoznám.')
    else:
        command.exec(context)

    # try:
    #     command = parse_line(line, commands)
    #     game_state = command.exec(current_room)
    # except AttributeError:  # CommandDoesntExist
    #     print('Taký príkaz nepoznám.')

    print()

outro()
