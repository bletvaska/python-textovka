#!/usr/bin/env python3
from random import randint

# 8. sprav funkciu, play_game(). a v nej sa odohrá jedna partia hry.
def play_game(secret=11):
    """
    Plays a signle round of game.

    This function runs a one round of a game. Goal is to find the secret number.

    :param secret: the secret number to find
    """

    # 1. pozdravis - myslim si cislo od 1 do 20
    print('Myslím si číslo od 1 do 20.')
    tip = None
    attempts = 1

    # 6. hraj, kym neuhadnes
    # 7. mas na to 5 pokusov a ked neuhadnes, tak vypis na obrazovku: Ta ty si jaká lama.
    while attempts <= 5:
        attempts += 1

        # 2. opytaj sa hraca na jeho tip
        s_tip = input('Tvoj tip: ')
        tip = int(s_tip)

        # 3. ak je tajne cislo mensie ako hracove, tak vypise na obrazovku: Hmm... Moje číslo je menšie ako tvoje.
        if secret < tip:
            print('Hmmm... Moje číslo je menšie ako tvoje.')

        # 4. ak je tajne cislo vacsie ako hracove, tak vypise na obrazovku: Hmm... Moje číslo je väčšie ako tvoje.
        elif secret > tip:
            print('Hmmm... Moje číslo je väčšie ako tvoje.')

        # 5. ak je tajne cislo rovne s hracovym, tak vypis: Ta ty genius.
        else:
            print('Ta ty genius!')
            break

    else:
        print(f'Ta ty si jaká lama. Moje tajné číslo bolo {secret}.')


if __name__ == '__main__':
    secret = randint(1, 20)
    play_game(secret)
    print('the end')
