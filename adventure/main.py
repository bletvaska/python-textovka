from rich import print

import states
from commands import About, Commands, Quit, Inventory
from helpers import intro, outro, parse_line

intro()

game_state = states.PLAYING
backpack = ['bic', 'padak']
commands = [
    About(),
    Commands(),
    Inventory(),
    Quit()
]


while game_state == states.PLAYING:
    line = input('> ').lower().lstrip().rstrip()

    if line == '':  # len(line) == 0
        continue

    cmd = parse_line(line, commands)
    if cmd is None:
        print('Taký príkaz nepoznám.')
    else:
        cmd.exec()

    # elif line == 'inventar':
    #     cmd = Inventory()
    #     cmd.exec(backpack)
    #
    # elif line == 'o hre':
    #     cmd = About()
    #     cmd.exec()
    #
    # elif line == 'prikazy':
    #     cmd = Commands()
    #     cmd.exec(commands)
    #
    # elif line == 'koniec':
    #     cmd = Quit()
    #     game_state = cmd.exec()
    #


outro()
