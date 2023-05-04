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

# game loop
while game_state == STATE_PLAYING:
    # get input from user
    line = input('> ').lower().lstrip().rstrip()

    # is input empty?
    if line == '':  # len(line) == 0
        continue

    # parse command
    for cmd in commands:
        if cmd.name == line:
            game_state = cmd.exec()
            break
    else:
        print('Taký príkaz nepoznám.')

outro()
