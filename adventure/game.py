#!/usr/bin/env python

import states
from commands import About, Commands, Quit, LookAround, Inventory, Examine, Take
from commands.drop import Drop
from context import Context
from helpers import intro, outro
from items.empty_seats import EmptySeats
from items.whip import Whip
from rooms.directions import DOWN
from rooms.in_plane import InPlane


def main():
    # init
    context = Context(
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

        current_room=InPlane(name='v lietadle',
                             description='Prebudil si sa v malom dvojmotorovom lietadle plachtiacom nad egyptskou púšťou. '
                                         'Je tu nádherný kľud, pretože motory sú vypnuté a na palube nie je okrem teba '
                                         'živej duše. (Celkom zaujímavá situácia, že áno?)',
                             items=[EmptySeats(), Whip()],
                             exits={
                                 DOWN: 'vo vzduchu'
                             })
    )

    # show room
    context.current_room.show()

    # game loop
    while context.game_state == states.PLAYING:
        line = input('> ').lstrip().rstrip().lower()

        if line == '':  # len(line) == 0
            continue

        for command in context.commands:
            if line.startswith(command.name):
                param = line.split(command.name)[1].strip()
                command.param = param
                command.exec(context)
                context.current_room.act(context)
                break
        else:
            print('Taký príkaz nepoznám.')

    if context.game_state not in (states.GAME_SOLVED, states.QUIT):
        print("Správa z tlače:\n"
              "Od nášho zvláštneho korešpondenta z Káhiry sme sa dozvedeli, že národný hrdina, miláčik čitateľov, "
              "nositeľ rádu za statočnosť, známy Indiana Jones, už bohužiaľ nie je medzi nami. Zomrel v egyptskej "
              "púšti, 31. apríla 1939, deň potom, ako si vybral svoju zaslúženú dovolenku. Jeho odchodom stráca naša "
              "spoločnosť jednu z najväčších postáv v dejinách Spojených Štátov. Veď to bol práve on, kto sa bez "
              "váhania\n"
              "(pokračovanie na str. 5)")


if __name__ == '__main__':
    intro()
    main()
    outro()
