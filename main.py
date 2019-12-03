#!/usr/bin/env python3
from commands import about, commands, go_west, go_east, go_down, quit
from context import Context
from room import DeadRoom

if __name__ == '__main__':
    context = Context()


    print('Indiana Jones and the Plane Escape')

    print(
        'Ta si sa zobudil v prvej triede lietadla spoločnosti Lao Che. To ticho ti až bilo do uší. Lietadlo vraj nikto nešoféruje a aj motory sú už vypnuté.')

    print(context.current_room)

    while context.game_state == 'PLAYING':
        line = input('> ').strip().lower()

        if line in ('koniec', 'quit', 'k', 'q'):
            quit(context)

        elif line in ('o autorovi', 'o mne', 'info'):
            about()

        elif line in ('prikazy', 'prikaz', 'commands'):
            commands()

        elif line in ('zapad', 'z', 'west', 'w'):
            go_west(context)

        elif line in ('vychod', 'v', 'east', 'e'):
            go_east(context)

        elif line in ('dolu', 'down'):
            go_down(context)

        else:
            print('taky prikaz nepoznam.')

        if isinstance(context.current_room, DeadRoom):
            print('GAME OVER')
            context.game_state = 'DEAD'
