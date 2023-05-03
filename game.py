from helpers import intro, outro
from states import STATE_PLAYING, STATE_QUIT

game_state = STATE_PLAYING

intro()

while game_state == STATE_PLAYING:
    line = input('> ').lower().lstrip().rstrip()

    if line == '':  # len(line) == 0
        continue

    elif line == 'o hre':
        print('Túto mocnú hru spáchal mocný programátor mirek')
        print('(c)2023 by mirek')

    elif line == 'pre evku':
        print('toto je vyrobene vylucne pre evku.')

    elif line == 'prikazy':
        print('Zoznam dostupných príkazov v hre:')
        print('* koniec - ukončí hru')
        print('* o hre - zobrazí informácie o hre')
        print('* príkazy - zobrazí zoznam dostupných príkazov v hre')

    elif line == 'koniec':
        question = input('Naozaj chceš skončiť? (ano/nie) ').lower().strip()
        if question == 'ano':
            game_state = STATE_QUIT

    else:
        print('Taký príkaz nepoznám.')

outro()
