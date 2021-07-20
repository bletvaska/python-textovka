#!/usr/bin/env python3
import random


def play_game(secret=7):
    # step 1
    print("Myslím si číslo od '1' do '20'.")
    # secret = 7
    tip = None
    counter = 5

    # step 5: hadaj, pokial neuhadnes
    while counter > 0 and secret != tip:
        # step 2
        tip = input('Tvoj tip: ')
        tip = int(tip)

        # step 3: Hmm... Moje je vacsie ako 3.
        if secret > tip:
            print(f'Hmm... Moje číslo je väčšie ako {tip}.')
            counter = counter - 1

        # step 4: aj mensie, aj genius
        elif secret < tip:
            print(f'Hmm... Moje číslo je menšie ako {tip}.')
            counter = counter - 1

        else:
            print('Ta ty si genius!')

    if counter == 0:
        print('Ta ty si husty, ale nestacilo')


if __name__ == '__main__':
    repeat = 'ano'

    while repeat == 'ano':
        play_game(random.randint(1, 20))
        repeat = input('Chceš si zahrať znova? (ano/nie) ')

    print('Ďakujem, že si si zahral túto mocnú hru.')

