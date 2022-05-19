#!/usr/bin/env python

if __name__ == '__main__':
    secret = 13
    print('Myslím si číslo od 1 do 20.')

    tip = None
    while tip != secret:
        tip = int(input('Tvoj tip: '))

        if tip > secret:
            print(f'Hmm... Moje číslo je menšie ako {tip}.')
        elif tip < secret:
            print(f'Hmm... Moje číslo je väčšie ako {tip}.')

    print('Ta ty si genius.')
