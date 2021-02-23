#!/usr/bin/env python
import random


def play_game(secret):
    print('Myslím si číslo od 1 do 20.')
    tip = None
    counter = 5

    while tip != secret and counter > 0:
        answer = input('Tvoj tip: ')
        tip = int(answer)

        if tip > secret:
            print(f'Hmm... Moje číslo je menšie ako {tip}.')

        elif tip < secret:
            print(f'Hmm... Moje číslo je väčšie ako {tip}.')

        else:
            print('Ta ty genius.')
            break

        counter = counter - 1
        if counter == 0:
            print('ty lama')


choice = 'a'

while choice == 'a':
    secret = random.randint(1, 20)
    play_game(secret)
    choice = input('Chceš si zahrať znova? (a/n) ')


print('goodbye')
