#!/usr/bin/env python3

line = None

print('Indiana Jones')

print('Nachádzaš sa v tmavej miestnosti, kde sa po stenách nachádzajú hieroglify z obdobia Juraja Jánošíka. Valaška a '
      'krpce sú najščastejším motívom, ktorý vidíš na vyrytých postavách na stene. Stiesňujúce miesto.')

while line != 'koniec':
    line = input('> ').lstrip().rstrip().lower()

    if len(line) == 0:  # line == ''
        continue

    elif line == 'o hre':
        print('Indiana Jones a jeho Pythoňácke dobrodružstvo')
        print('Nestarnúci hrdina Indiana Jones sa tentokrát ocitol sám pustý v škaredej miestnosti. A jedine '
              'Pythoňácky programátori mu môžu zachrániť krk. Je to na tebe.')
        print('\n(c) 2021 hru spáchal mirek')

    elif line == 'rozhliadni sa':
        print('Nachádzaš sa v tmavej miestnosti, kde sa po stenách nachádzajú hieroglify z obdobia Juraja Jánošíka. '
              'Valaška a krpce sú najščastejším motívom, ktorý vidíš na vyrytých postavách na stene. Stiesňujúce '
              'miesto.')

    else:
        print('Tento príkaz nepoznám.')
