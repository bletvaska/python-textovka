from rich import print

import states
from commands import About, Commands
from helpers import intro, outro

intro()

game_state = states.PLAYING

while game_state == states.PLAYING:
    line = input('> ').lower().lstrip().rstrip()

    if line == '':  # len(line) == 0
        continue

    elif line == 'o hre':
        cmd = About()
        cmd.exec()

    elif line == 'prikazy':
        cmd = Commands()
        cmd.exec()

    elif line == 'koniec':
        game_state = states.QUIT

    else:
        print('Taký príkaz nepoznám.')

outro()
