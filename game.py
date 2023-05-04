from commands import About, Commands, Quit, LookAround
from helpers import intro, outro
from rooms import Airplane
from states import STATE_PLAYING

game_state = STATE_PLAYING
commands = [
    About(),
    Commands(),
    LookAround(),
    Quit(),
]
current_room = Airplane()

intro()

# show room
print(current_room.description)

print('Vidíš:')
for item in current_room.items:
    print(f'  {item}')

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
            game_state = cmd.exec(current_room)
            break
    else:
        print('Taký príkaz nepoznám.')

outro()
