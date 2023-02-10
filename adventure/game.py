#!/usr/bin/env python

from rich import print

import states
from commands import *
from game_context import GameContext
from helpers import intro, outro, parse_line, get_room_by_name


def main():
    # game initialization
    context = GameContext(
        commands=[
            About(),
            Commands(),
            Down(),
            Drop(),
            East(),
            Examine(),
            Help(),
            Inventory(),
            Load(),
            LookAround(),
            North(),
            Quit(),
            Save(),
            Score(),
            South(),
            Take(),
            Up(),
            Use(),
            West()
        ]
    )

    context.current_room = get_room_by_name('v lietadle', context)
    context.current_room.show()

    # game loop
    while context.game_state == states.PLAYING:
        line = input('> ').lstrip().rstrip().lower()

        if line == '':  # len(line) == 0
            continue
            # pass

        # parse command line
        command = parse_line(line, context)
        if command is None:
            print('[red]Tento príkaz nepoznám.[/red]')
        else:
            command.exec(context)
            context.current_room.act(context)

    if context.game_state == states.WELL_DONE:
        print('A tak sa skončila ďalšia epizóda v dobrodružnom živote Indiana Jonesa. A to, že ju v zdraví prežil, '
              'je len tvojou zásluhou! Za peniaze, ktoré získal za náhrdelník, si teraz môže Indy konečne dopriať '
              'kľudnú dovolenku...')

        print()
        print('...alebo? (To sa ukáže časom)')

        print()
        print(f'Hru si zvládol na [bold yellow]{context.score}%[/bold yellow].')


if __name__ == '__main__':
    intro()
    main()
    outro()
