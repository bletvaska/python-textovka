from commands.about import About
from commands.commands import Commands
from commands.inventory import Inventory
from commands.look_around import LookAround
from commands.quit import Quit
from game_context import GameContext
from helpers import intro, outro
from rooms.airplane import Airplane
from states import STATE_PLAYING

# game initialization
context = GameContext(
    current_room=Airplane(),
    commands=[
        About(),
        Commands(),
        Inventory(),
        LookAround(),
        Quit(),
    ]
)

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
    for cmd in context.commands:
        if cmd.name == line:
            cmd.exec(context)
            break
    else:
        print('Taký príkaz nepoznám.')

outro()
