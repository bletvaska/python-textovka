#!/usr/bin/env python3
import states
from commands.about import About
from commands.commands import Commands
from commands.look_around import LookAround
from commands.quit import Quit
from helpers import intro, outro, parse_line
from items.empty_seats import EmptySeats
from items.whip import Whip
from rooms.room import Room

# game initialization
game_state = states.PLAYING
commands = [
    About(),
    Commands(),
    LookAround(),
    Quit(),
]

current_room = Room(
    name='v lietadle',
    description='Prebudil si sa v malom dvojmotorovom lietadle plachtiacom nad egyptskou púšťou. Je '
                'tu nádherný kľud, pretože motory sú vypnuté a na palube nie je okrem teba živej '
                'duše. (Celkom zaujímavá situácia, že áno?)',
    items=[Whip(), EmptySeats()],
    # exits=[]
)

# game loop
intro()
current_room.show()

while game_state == states.PLAYING:
    line = input('> ').lower().lstrip().rstrip()  # echo line | lower | lstrip | rstrip

    # is line empty?
    if line == '':  # if len(line) == 0:
        continue  # {}

    # parse and execute command
    command = parse_line(line, commands)
    if command is None:
        print('Taký príkaz nepoznám.')
    else:
        game_state = command.exec(current_room)

    # try:
    #     command = parse_line(line, commands)
    #     game_state = command.exec(current_room)
    # except AttributeError:  # CommandDoesntExist
    #     print('Taký príkaz nepoznám.')

outro()
