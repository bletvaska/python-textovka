#!/usr/bin/env python3

print('Nachádzaš sa v tmavej miestnosti. Každé okno je zvonku zabarikádované a do miestnosti preniká len úzky prameň '
      'svetla. Masívne drevené dvere sú jediným východom z miestnosti.')

line = None

while line != 'koniec':
    line = input('> ').strip().lower()

    if line == 'o hre':
        print('Hru spáchal v (c) 2021 mirek.')
        print('Ďalšie dobrodužstvo Indiana Jonesa. Tentokrát sa pokúsi o únik zo skladu Košického Technického múzea.')

    elif line == 'prikazy':
        print('Zoznam príkazov hry:')

        print('* koniec - ukončí rozohratú hru')
        print('* o hre - zobrazí informácie o hre')
        print('* prikazy - zobrazí zoznam príkazov dostupných v hre')
        print('* rozhliadni sa - zobrazí obsah miestnosti')

    elif line == 'koniec':  # quit, bye, q
        print('ta koncime')

    else:
        print('Taký príkaz nepoznám.')

print('...koniec...')
