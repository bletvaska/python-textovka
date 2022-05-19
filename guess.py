#!/usr/bin/env python

if __name__ == '__main__':
    secret = 13
    print('Myslím si číslo od 1 do 20.')

    tip = None
    count = 0
    while tip != secret and count < 5:
        tip = int(input('Tvoj tip: '))
        count += 1

        if tip > secret:
            print(f'Hmm... Moje číslo je menšie ako {tip}.')
        elif tip < secret:
            print(f'Hmm... Moje číslo je väčšie ako {tip}.')
        else:
            print('Ta ty si genius.')
            break
    else:
    # if tip != secret:
        print('Ta ty si jaká lama.')

    print('(c)2022 by mirek')
