#!/usr/bin/env python
from commands.about import About
from commands.commands import Commands
from commands.inventory import Inventory
from commands.quit import Quit
from helpers import intro, outro
from states import STATE_PLAYING, STATE_QUIT


# main building blocks

# * miestnosti (lokacia, place)
#   * opis
#   * zoznam predmetov v miestnosti
#   * nazov
#   * vychody (susedia)


# * predmety
#   * nazov
#   * opis
#   * vlastnosti
#   + pouzitie predmetu()
#   + preskumanie predmetu()

# kde sa nachadzam

intro()
game_state = STATE_PLAYING
backpack = ['revolver', 'bic']
commands = [
    About(),
    Commands(),
    Inventory(),
    Quit()
]

while game_state == STATE_PLAYING:
    line = input('> ').lstrip().rstrip().lower()

    if line == '':  # len(line) == 0
        continue
        # pass

    for command in commands:
        if line == command.name:
            command.exec(backpack)
            break
    else:
        print('Tento príkaz nepoznám.')

outro()
