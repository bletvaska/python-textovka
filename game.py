#!/usr/bin/env python3

def show_room(room):
    print(f'Nachádzaš sa v miestnosti {room["name"]}')
    print(room['description'])
    print()

if __name__ == '__main__':
    print(' ___           _ _                         _                       ')
    print('|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ')
    print(" | || '_ \ / _` | |/ _` | '_ \ / _` |  _  | |/ _ \| '_ \ / _ \/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\__ \\")
    print('|___|_| |_|\__,_|_|\__,_|_| |_|\__,_|  \___/ \___/|_| |_|\___||___/')

    print('                                                     (c) 2021 mirek')

    room = {
        'description': 'Nachádzaš v tmavej miestnosti. Kamenné múry dávajú tušiť, že sa nachádzaš v nejakej kamennej kobke. Žeby podzemie hradu v Grunwalde? Okná tu nie sú žiadne, čo by ťa uistili o správnosti tohto predpokladu.',
        'name': 'kobka',
        'items': None,
        'exits': None
    }

    show_room(room)

    line = None

    while line != 'koniec':
        line = input('> ').rstrip().lstrip().lower()

        if line == 'o hre':
            print('Hru spáchal  (c)2021 mirek')
            print('Ďalší príbeh Indiana Jonesa sa odohráva v temnej komôrke.')
            print()

        elif line == 'rozhliadni sa':
            show_room(room)

        elif line == 'prikazy':
            print('Dostupné príkazy v hre:')
            print('* koniec - ukončí rozohratú hru')
            print('* o hre - zobrazí informácie o fantastickom autorovi hry a o hre samotnej')
            print('* prikazy - zobrazí zoznam príkazov, ktoré hra podporuje')
            print()

        elif line in ('koniec', ''):
            continue

        else:
            print('Taký príkaz nepoznám.')
