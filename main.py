import states
from commands import About, Commands, Quit, Inventory
from helpers import intro, outro

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
        pass

    elif line == 'o hre':
        about = About()
        game_state = about.exec(backpack)

    elif line == 'prikazy':
        commands = Commands()
        game_state = commands.exec(backpack, commands)

    elif line == 'koniec':
        cmd = Quit()
        game_state = cmd.exec(backpack)

    elif line == 'inventar':
        cmd = Inventory()
        game_state = cmd.exec(backpack)

    else:
        print('Taký príkaz nepoznám.')

outro()
