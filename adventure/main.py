from rich import print
from traitlets.utils.descriptions import describe

import states
from game_context import GameContext
from helpers import intro, outro, parse_line
from rooms.room import Room

intro()

# game initialization
context = GameContext()
context.current_room = Room(
    name='lietadlo',
    description='Prebudil si sa v malom dvojmotorovom lietadle plachtiacom nad egyptskou púšťou. Je tu nádherný kľud, pretože motory sú vypnuté a na palube nie je okrem teba živej duše. (Celkom zaujímavá situácia, že áno?)',
    items=['bič', 'prázdne sedadlá'],
)

# game loop
while context.game_state == states.PLAYING:
    line = input('> ').lower().lstrip().rstrip()

    if line == '':  # len(line) == 0
        continue

    cmd = parse_line(line, context.commands)
    if cmd is None:
        print('Taký príkaz nepoznám.')
    else:
        cmd.exec(context)

outro()
