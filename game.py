from commands.about import About
from commands.commands import Commands
from commands.drop import Drop
from commands.examine import Examine
from commands.inventory import Inventory
from commands.look_around import LookAround
from commands.quit import Quit
from commands.take import Take
from game_context import GameContext
from helpers import intro, outro
from items.whip import Whip
from rooms.airplane import Airplane
from states import STATE_PLAYING

# game initialization
context = GameContext(
    current_room=Airplane(),
    commands=[
        About(),
        Commands(),
        Drop(),
        Examine(),
        Inventory(),
        LookAround(),
        Quit(),
        Take(),
    ]
)
# context.backpack.append(Whip())

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
        if line.startswith(cmd.name):
            # extract/parse command parameter
            param = line.split(cmd.name)[1].strip()

            # prepare and execute command
            cmd.param = param
            cmd.exec(context)

            # make action in room
            context.current_room.act(context)

            break
    else:
        print('Taký príkaz nepoznám.')

outro()
