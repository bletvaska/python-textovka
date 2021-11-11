#!/usr/bin/env python3
import random


def play_game(secret=7):
    print('Myslím si číslo od "1" do "20".')
    tip = None
    counter = 5

    while counter > 0 and tip != secret:
        tip = input('Tvoj tip: ')
        tip = int(tip)

        if secret > tip:
            print('Hmm… Moje číslo je väčšie ako tvoje.')
            counter -= 1
        elif secret < tip:
            print('Hmm… Moje číslo je menšie ako tvoje.')
            counter -= 1
        else:
            print('Ta ty genius.')
            break
    else:
        print(f'Ta ty si lama. Ta si to neuhadol. Moje tajne cislo je {secret}.')


# def main():
if __name__ == '__main__':
    playing = 'a'

    while playing in ('a', 'ano', 'y', 'yes'):
        play_game(random.randint(1, 20))
        playing = input('Chces hrat znova? (a/n) ').lstrip().rstrip().lower()

    print(
        'Ta tuto mocnu hru spachal zacinajuci herny vyvojar mirek. Ak ho cches podporit, tak cvakni na ucet SK1234567890.')
