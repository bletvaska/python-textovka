#!/usr/bin/env python
import states
from commands import About, Commands, Quit
from helpers import intro, outro
from rooms import Room

# intro
intro()

# init
game_state = states.PLAYING
commands = [
    About(),
    Commands(),
    Quit()
]
current_room = Room(name='v lietadle',
                    description='Prebudil si sa v malom dvojmotorovom lietadle plachtiacom nad egyptskou púšťou. Je '
                                'tu nádherný kľud, pretože motory sú vypnuté a na palube nie je okrem teba živej '
                                'duše. (Celkom zaujímavá situácia, že áno?)',
                    items=['bič', 'prázdne sedadlá'],
                    exits=[])

# show room
print(current_room.description)
if current_room.items != []:  # len(current_room.items) > 0
    print('Vidíš:')
    for item in current_room.items:
        print(f'  {item}')
else:
    print('Nevidíš tu nič zvláštne.')

# game loop
while game_state == states.PLAYING:
    line = input('> ').lstrip().rstrip().lower()

    if line == '':  # len(line) == 0
        continue

    for command in commands:
        if command.name == line:
            game_state = command.exec()
            break
    else:
        print('Taký príkaz nepoznám.')

outro()
