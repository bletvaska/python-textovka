#!/usr/bin/env python3
from random import randint


def play_game(secret):
    print('Myslím si číslo od 1 do 20.')
    tip = None
    count = 0

    while secret != tip and count < 5:
        tip = input(f"Tvoj {count + 1}. tip: ")
        tip = int(tip)
        count += 1

        if tip > secret:
            print(f'Hmm... Moje číslo je menšie ako {tip}.')
        elif tip < secret:
            print(f'Hmm... Moje číslo je väčšie ako {tip}.')
        else:
            print(f'Ta ty genius!!!')
            break
    else:
        print('ta ty jaka lama. sa nauc pajton najprv, hej?')


playing = True
play_game(randint(1, 20))
while playing == True:
    choice = input('Chceš hrať túto mocnú hru ešte raz? (a/n) ')
    if choice == 'a':
        play_game(randint(1, 20))
    else:
        playing = False

print(
    'Ta díky, že si si zahral túto mocnú hru. Prosím podpor nádejného autora svojím malým príspevkom na účet SK123456789008765433121. Bude ti vďačný za každý tvoj príspevok nad 100 evry. Keď nepošleš, nech ťa svokra skára.')
print('(c) 2021 spáchal mirek')
