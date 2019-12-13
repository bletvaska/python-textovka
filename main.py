#!/usr/bin/env python3
from commands.command import Command
from context import Context
from room import DeadRoom
# from commands import Commands, About, Quit, West, East, Down
from commands import *

if __name__ == '__main__':
    context = Context()

    print('Indiana Jones and the Plane Escape')

    print(
        'Ta si sa zobudil v prvej triede lietadla spoločnosti Lao Che. To ticho ti až bilo do uší. Lietadlo vraj nikto nešoféruje a aj motory sú už vypnuté.')

    print(context.current_room)

    commands = [About(), Quit(), West(), East(), Down(), LookAround()]
    commands.append(Commands(commands))

    while context.game_state == 'PLAYING':
        line = input('> ').strip().lower()

        for command in commands:
            if command._name == line:
                command.exec(context)
                break
        else:
            print('taky prikaz nepoznam.')

        if isinstance(context.current_room, DeadRoom):
            print('GAME OVER')
            context.game_state = 'DEAD'
