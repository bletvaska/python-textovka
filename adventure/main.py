from rich import print

import states
from commands.about import About
from commands.commands import Commands
from commands.inventory import Inventory
from commands.quit import Quit
from helpers import intro, outro, parse_line

intro()

game_state = states.PLAYING
backpack = ['bic', 'padak']
commands = [
    About(),
    Commands(),
    Inventory(),
    Quit()
]

while game_state == states.PLAYING:
    line = input('> ').lower().lstrip().rstrip()

    if line == '':  # len(line) == 0
        continue

    cmd = parse_line(line, commands)
    if cmd is None:
        print('Taký príkaz nepoznám.')
    else:
        game_state = cmd.exec(context)

outro()
