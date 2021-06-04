import states
from context import GameContext
from command import *


def parse(context, line, commands):
    for cmd in commands:
        for alias in cmd.aliases:
            if line.startswith(alias):
                cmd.params = line.replace(alias, '').strip()
                return cmd

    return None


if __name__ == '__main__':
    # initialization
    context = GameContext()

    commands = [
        About(),
        Use(),
        Quit()
    ]

    context.room.show_room()

    # game loop
    while context.state == states.STATE_PLAYING:
        # parsovanie vstupu
        line = input('> ').strip()

        cmd = parse(context, line, commands)
        if cmd is None:
            print('Taký príkaz nepoznám.')
        else:
            cmd.exec(context)

    print('good bye')
