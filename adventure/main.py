from rich import print

import states
from commands import About
from helpers import intro, outro

intro()

game_state = states.PLAYING

while game_state == states.PLAYING:
    line = input('> ').lower().lstrip().rstrip()

    if line == '':  # len(line) == 0
        continue

    elif line == 'o hre':
        cmd = About()
        cmd.exec()

    elif line == 'prikazy':
        print('V hre je možné použiť tieto príkazy:')
        print('* [bold cyan]o hre[/bold cyan] - zobrazí informácie o hre')
        print('* [bold cyan]prikazy[/bold cyan] - zobrazí zoznam dostupných príkazov v hre')
        print('* [bold cyan]koniec[/bold cyan] - ukončí rozohratú hru')

    elif line == 'koniec':
        game_state = states.QUIT

    else:
        print('Taký príkaz nepoznám.')

outro()
