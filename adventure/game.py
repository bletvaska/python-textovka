#!/usr/bin/env python

import states
from commands import About, Commands, Quit, LookAround, Inventory, Examine, Take, Down, East, North, South, Up, West, \
    Drop, Use, Save, Load
from context import Context
from helpers import intro, outro, get_room_by_name, victory
from rooms.world import load_world


def main():
    # game init
    world = load_world()
    context = Context(
        commands=[
            About(),
            Commands(),
            Down(),
            Drop(),
            East(),
            Examine(),
            Inventory(),
            Load(),
            LookAround(),
            North(),
            Quit(),
            Save(),
            South(),
            Take(),
            Up(),
            Use(),
            West(),
        ],
        world=world,
        current_room=get_room_by_name('oáza', world),
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
                # execute command
                param = line.split(command.name)[1].strip()
                command.param = param
                command.exec(context)

                # make action in room
                context.current_room.act(context)
                break
        else:
            print('Taký príkaz nepoznám.')

    # death of indiana jones in press
    if context.game_state not in (states.GAME_SOLVED, states.QUIT):
        print("Správa z tlače:\n"
              "Od nášho zvláštneho korešpondenta z Káhiry sme sa dozvedeli, že národný hrdina, miláčik čitateľov, "
              "nositeľ rádu za statočnosť, známy Indiana Jones, už bohužiaľ nie je medzi nami. Zomrel v egyptskej "
              "púšti, 31. apríla 1939, deň potom, ako si vybral svoju zaslúženú dovolenku. Jeho odchodom stráca naša "
              "spoločnosť jednu z najväčších postáv v dejinách Spojených Štátov. Veď to bol práve on, kto sa bez "
              "váhania\n"
              "(pokračovanie na str. 5)")

    # victory screen
    if context.game_state == states.GAME_SOLVED:
        victory()


if __name__ == '__main__':
    intro()
    main()
    outro()
