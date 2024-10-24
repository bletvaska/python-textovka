import states
from commands import About, Commands, Quit
from helpers import intro, outro

intro()

game_state = states.PLAYING   # states.PLAYING
while game_state == states.PLAYING:
    line = input('> ').lstrip().rstrip().lower()

    if line == '':
        pass

    elif line == 'o hre':
        about = About()
        game_state = about.exec()

    elif line == 'prikazy':
        commands = Commands()
        game_state = commands.exec()

    elif line == 'koniec':
        cmd = Quit()
        game_state = cmd.exec()

    else:
        print('Taký príkaz nepoznám.')

outro()
