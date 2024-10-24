import states
from commands.about import About
from commands.commands import Commands
from commands.inventory import Inventory
from commands.quit import Quit
from game_context import GameContext
from helpers import intro, outro, parse_line

intro()

# game initialization
context = GameContext(
    commands=[
        About(),
        Commands(),
        Inventory(),
        Quit()
    ]
)

# game loop
while context.game_state == states.PLAYING:
    line = input('> ').lstrip().rstrip().lower()

    if line == '':
        continue

    command = parse_line(line, context.commands)
    if command is None:
        print('Taký príkaz nepoznám.')
    else:
        command.exec(context)

outro()
