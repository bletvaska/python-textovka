from commands import About, Commands, Quit
from helpers import intro, outro
from states import STATE_PLAYING, STATE_QUIT

game_state = STATE_PLAYING

intro()

while game_state == STATE_PLAYING:
    line = input('> ').lower().lstrip().rstrip()

    if line == '':  # len(line) == 0
        continue

    elif line == 'o hre':
        About().exec()

    elif line == 'prikazy':
        Commands().exec()

    elif line == 'koniec':
        Quit().exec()

    else:
        print('Taký príkaz nepoznám.')

outro()
