#!/usr/bin/env python3
from context import Context
from room import DeadRoom
from commands import *

if __name__ == '__main__':
    context = Context()

    print('Indiana Jones and the Plane Escape')

    print(
        'Ta si sa zobudil v prvej triede lietadla spoločnosti Lao Che. To ticho ti až bilo do uší. Lietadlo vraj nikto nešoféruje a aj motory sú už vypnuté.')

    print(context.current_room)



    while context.game_state == 'PLAYING':
        line = input('> ').strip().lower()

        command = context.parser.parse(line)

        if command is not None:
            command.exec(context)
        else:
            print('taky prikaz nepoznam.')

        if isinstance(context.current_room, DeadRoom):
            print('GAME OVER')
            context.game_state = 'DEAD'
