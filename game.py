from commands import About, Commands, Quit, LookAround, Inventory
from game_context import GameContext
from helpers import intro, outro
from items import Whip
from rooms import Airplane
from states import STATE_PLAYING

context = GameContext(
    current_room=Airplane()
)
context.backpack.append(Whip())

commands = [
    About(),
    Commands(),
    Inventory(),
    LookAround(),
    Quit(),
]

intro()

# show room
context.current_room.show()

# game loop
while context.game_state == STATE_PLAYING:
    # get input from user
    line = input('> ').lower().lstrip().rstrip()

    # is input empty?
    if line == '':  # len(line) == 0
        continue

    # parse command
    for cmd in commands:
        if cmd.name == line:
            cmd.exec(context)
            break
    else:
        print('Taký príkaz nepoznám.')

outro()
