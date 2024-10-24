import states
from commands.about import About
from commands.commands import Commands
from commands.inventory import Inventory
from commands.quit import Quit
from helpers import intro, outro, parse_line

intro()

# game initialization
backpack = ['bic', 'slivovica']
game_state = states.PLAYING
commands = [
    About(),
    Commands(),
    Inventory(),
    Quit()
]

# game loop
while game_state == states.PLAYING:
    line = input('> ').lstrip().rstrip().lower()

    if line == '':
        continue

    command = parse_line(line, commands)
    if command is None:
        print('Taký príkaz nepoznám.')
    else:
        game_state = command.exec(backpack, commands)

outro()
