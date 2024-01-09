#!/usr/bin/env python3
import states
from helpers import intro, outro

intro()

game_state = states.PLAYING
while game_state == states.PLAYING:
    line = input('> ').lower().lstrip().rstrip()  # echo line | lower | lstrip | rstrip

    if line == '':  # if len(line) == 0:
        pass  # {}

    elif line == 'o hre':
        print('(c)2024 created by mirek')
        print('Dalsie dobrodruzstvo indiana jonesa tentokrat vytvorene v jazyku Python.')

    elif line == 'prikazy':
        print('V hre je možné použiť tieto príkazy:')
        print('* koniec - ukončí rozhratú hru')
        print('* o hre - zobrazí informácie o hre')
        print('* prikazy - zobrazí zoznam dostupných príkazov v hre')

    elif line == 'koniec':
        choice = input('Naozaj chceš skončiť? (a/n) ').lower().strip()
        if choice in ('a', 'y', 'ano', 'yes'):
            print('Ďakujem, že si si zahral túto úžasnú (ukradnutú) hru.')
            game_state = states.QUIT

    else:
        print('Taký príkaz nepoznám.')

outro()
