#!/usr/bin/env python

def show_room(room):
    print(f'Nachádzaš sa v miestnosti {room["name"]}.')
    print(room['description'])
    print(room['exits'])


line = None

"""
+-------+     +-------------+
|  hall |-----| living room |
+-------+     +-------------+          N
    |                                  ^
    |                              W < o > E
+---------+                            v
| dungeon |                            S
+---------+
"""

world = {
    'chodba': {
        'description': 'Nachádzaš sa v chodbe neznámeho bytu. Vchodové dvere sú uspešne zamknuté. Veci visiace na vešiakoch rozhodne nie sú tvoje. Ale... ani by si si ich na seba nedal.',
        'name': 'chodba',
        'exits': {
            'east': 'obyvacka',
            'west': None,
            'north': None,
            'south': 'spajza'
        },
        'items': ''
    },
    'obyvacka':  {
        'description': 'Nachádzaš sa (zrejme) v obyvačke tohto nehostinného bytu. Pôvodný majiteľ nechal po sebe na stenách pomerne nevkusné tapety. Hádam ešte zo sociku. Okno, ktoré tu prepúšťa aspoň tú trochu slnečných lúčov pomedzi diery v kartónoch je aj tak zamrežované.',
        'name': 'obyvacka',
        'exits': {
            'east': None,
            'west': 'chodba',
            'north': None,
            'south': None
        },
        'items': ''
    },
    'spajza': {
        'description': 'Je tu temno a vlhko. Kompóty na poličkách dotvárajú temnú atmostféru tejto miestnosti.',
        'name': 'spajza',
        'exits': {
            'east': None,
            'west': None,
            'north': 'chodba',
            'south': None
        },
        'items': ''
    }
}


current_room = world['chodba']


print(' _____                            ____                       ')
print('| ____|___  ___ __ _ _ __   ___  |  _ \ ___   ___  _ __ ___  ')
print('|  _| / __|/ __/ _` | \'_ \\ / _ \\ | |_) / _ \\ / _ \\| \'_ ` _ \\ ')
print('| |___\__ \ (_| (_| | |_) |  __/ |  _ < (_) | (_) | | | | | |')
print('|_____|___/\___\__,_| .__/ \___| |_| \_\___/ \___/|_| |_| |_|')
print('                    |_|                                      ')
print('                                   (c)2021 Python 101 Version')
print()

show_room(current_room)

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
        print('rozhliadni sa - zobrazí opis aktuálnej miestnosti')

    elif line == 'vychod':
        current_room = world['obyvacka']
        show_room(current_room)

    elif line == 'zapad':
        current_room = world['chodba']
        show_room(current_room)

    elif line == 'rozhliadni sa':
        show_room(current_room)

    else:
        print("Tento príkaz nepoznám.")

print('Toto je koniec. Díky, že si si zahral.')
