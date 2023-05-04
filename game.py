from commands import About, Commands, Quit
from helpers import intro, outro
from states import STATE_PLAYING, STATE_QUIT

game_state = STATE_PLAYING
commands = [
    About(),
    Commands(),
    Quit(),
]

intro()

while game_state == STATE_PLAYING:
    line = input('> ').lower().lstrip().rstrip()

    for cmd in commands:
        if cmd.name == line:
            cmd.exec()
            break
    else:
        print('Taký príkaz nepoznám.')

    # if line == '':  # len(line) == 0
    #     continue
    #
    # elif line == 'o hre':
    #     About().exec()
    #
    # elif line == 'prikazy':
    #     Commands().exec()
    #
    # elif line == 'koniec':
    #     game_state = Quit().exec()
    #
    # else:
    #     print('Taký príkaz nepoznám.')

outro()
