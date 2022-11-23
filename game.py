#!/usr/bin/env python
from helpers import intro, outro
from states import STATE_PLAYING, STATE_QUIT


# main building blocks

# * miestnosti (lokacia, place)
#   * opis
#   * zoznam predmetov v miestnosti
#   * nazov
#   * vychody (susedia)


# * predmety
#   * nazov
#   * opis
#   * vlastnosti
#   + pouzitie predmetu()
#   + preskumanie predmetu()

# kde sa nachadzam

intro()
game_state = STATE_PLAYING
backpack = ['revolver', 'bic']

while game_state == STATE_PLAYING:
    line = input('> ').lstrip().rstrip().lower()

    if line == '':
        continue
        # pass

    elif line == 'o hre':
        print('Hru Indiana Jones 2 napísal mladý nádejný programátor v jazyku Python - mirek v roku 2022.')

    elif line == 'prikazy':
        print('V hre je možné použiť tieto príkazy:')
        print('* inventar - zobrazi obsah hráčovho batohu')
        print('* koniec - ukončí hru')
        print('* o hre - zobrazi informacie o hre')
        print('* prikazy - zoznam dostupných príkazov v hre')

    elif line == 'koniec':
        choice = input('Naozaj chceš ukončiť hru? (y/n) ').lstrip().rstrip().lower()
        if choice in ('y', 'yes', 'a', 'ano'):
            game_state = STATE_QUIT

    elif line == 'inventar':
        if len(backpack) == 0:
            print('Batoh je prázdny.')
        else:
            print('V batohu máš:')
            for item in backpack:
                print(item)

    else:
        print('Tento príkaz nepoznám.')

outro()
