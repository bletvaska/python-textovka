#!/usr/bin/env python

line = None

print(' _____                            ____                       ')
print('| ____|___  ___ __ _ _ __   ___  |  _ \ ___   ___  _ __ ___  ')
print('|  _| / __|/ __/ _` | \'_ \\ / _ \\ | |_) / _ \\ / _ \\| \'_ ` _ \\ ')
print('| |___\__ \ (_| (_| | |_) |  __/ |  _ < (_) | (_) | | | | | |')
print('|_____|___/\___\__,_| .__/ \___| |_| \_\___/ \___/|_| |_| |_|')
print('                    |_|                                      ')
print('                                   (c)2021 Python 101 Version')
print()

print('Nachádzaš sa v chodbe neznámeho bytu. Vchodové dvere sú uspešne zamknuté. Veci visiace na vešiakoch rozhodne nie sú tvoje. Ale... ani by si si ich na seba nedal.')
print('Môžeš ísť na západ.')

while line != 'koniec':
    line = input('> ').strip().lower()

    if line == 'o hre':
        print('(c)2021 by mirek na mocnom Pythoňáckom kurze spáchal.')
        print('Táto mocná hra je o...')

    elif line == 'prikazy':
        print('Zoznam akutálne dostupných príkazov:')
        print('o hre - zobrazí informácie o hre')
        print('koniec - ukončí hru')
        print('prikazy - zobrazi zoznam prikazov')
        print('zapad - prejdeš na západ')

    elif line == 'zapad':
        print('Nachádzaš sa (zrejme) v obyvačke tohto nehostinného bytu. Pôvodný majiteľ nechal po sebe na stenách pomerne nevkusné tapety. Hádam ešte zo sociku. Okno, ktoré tu prepúšťa aspoň tú trochu slnečných lúčov pomedzi diery v kartónoch je aj tak zamrežované.')
        print('Môžeš ísť na východ.')

    else:
        print("Tento príkaz nepoznám.")

print('Toto je koniec. Díky, že si si zahral.')
