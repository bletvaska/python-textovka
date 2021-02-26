#!/usr/bin/env python
from commands import *
import json


line = None

"""
+--------+
| heaven |
+--------+
    |
    |
    v
+-------+     +-------------+
|  hall |<--->| living room |
+-------+     +-------------+
    ^                                  N
    |                                  ^
    v                              W < o > E
+---------+                            v
| dungeon |                            S
+---------+
"""

# nacitanie sveta z json suboru
file = open('world.json', 'r', encoding='utf-8')
world = json.load(file)
file.close()

# rozmiestnenie veci do sveta
teplaky = {
    'name': 'teplaky',
    'description': 'Parádne tepláky ružovej farby. Asi pána domáceho. Súdiac podľa veľkosti.',
    'features': ['movable', ]
}

kanister = {
    'name': 'kanister',
    'description': 'Vojenský kanister na 20l. Odštroboval si zátku, čuchol si a rovno si ju zašroboval naspäť. Fuj benzín. Ešte že nie som fajčiar.',
    'features': ['movable', 'usable']
}

dvere = {
    'name': 'vchodove dvere',
    'description': 'Masívne dubové vchodové dvere s dvoma zámkami. Toto asi nebude len tak obyčaný bytík nejakého študentíka.',
    'features': []
}

zapalky = {
    'name': 'zapalky',
    'description': 'Zapalky v pocte kusov 10. ',
    'features': ['movable', 'usable']
}

bucket = {
    'name': 'vedro',
    'description': 'Vedro s vodou',
    'features': ['movable', 'usable']
}


world['chodba']['items'].append(dvere)

# world['chodba']['items'].append(teplaky)
# world['chodba']['items'].append(kanister)


# game init
current_room = world['chodba']
backpack = []
backpack.append(kanister)
backpack.append(teplaky)
backpack.append(zapalky)
backpack.append(bucket)


print(' _____                            ____                       ')
print('| ____|___  ___ __ _ _ __   ___  |  _ \ ___   ___  _ __ ___  ')
print('|  _| / __|/ __/ _` | \'_ \\ / _ \\ | |_) / _ \\ / _ \\| \'_ ` _ \\ ')
print('| |___\__ \ (_| (_| | |_) |  __/ |  _ < (_) | (_) | | | | | |')
print('|_____|___/\___\__,_| .__/ \___| |_| \_\___/ \___/|_| |_| |_|')
print('                    |_|                                      ')
print('                                   (c)2021 Python 101 Version')
print()

show_room(current_room)

while line not in ('koniec', 'quit', 'exit', 'q', 'end', 'x'):
    line = input('> ').strip().lower()

    if line == 'o hre':
        cmd_about()

    elif line == 'prikazy':
        cmd_commands()

    elif line in ('vychod', 'v', 'east', 'e'):
        current_room = cmd_east(current_room, world)

    elif line in ('zapad', 'z', 'west', 'w'):
        current_room = cmd_west(current_room, world)

    elif line in ('juh', 'j', 'south'):
        current_room = cmd_south(current_room, world)

    elif line in ('sever', 's', 'north', 'n'):
        current_room = cmd_north(current_room, world)

    elif line == 'rozhliadni sa':
        cmd_look_around(current_room)

    elif line in ('inventar', 'i'):
        cmd_inventory(backpack)

    elif line.startswith('preskumaj'):
        cmd_explore(backpack, current_room, line)

    elif line.startswith('poloz'):
        cmd_drop(backpack, current_room, line)

    elif line.startswith('vezmi'):
        cmd_take(backpack, current_room, line)

    elif line.startswith('pouzi'):
        cmd_use(backpack, current_room, line)

    elif line not in ('koniec', 'quit', 'exit', 'q', 'end', 'x'):
        break

    else:
        print("Tento príkaz nepoznám.")

    # vyhodnotenie, ci som hru skoncil
    if current_room['name'] == 'sloboda':
        print(" _____                  _                 ")
        print("|  ___| __ ___  ___  __| | ___  _ __ ___  ")
        print("| |_ | '__/ _ \/ _ \/ _` |/ _ \| '_ ` _ \ ")
        print("|  _|| | |  __/  __/ (_| | (_) | | | | | |")
        print("|_|  |_|  \___|\___|\__,_|\___/|_| |_| |_|")
        print()
        print('A konečne si slobodný. Si sa kukol na prsteník, že fakt a fakt. Slobodaaaaaaaa.')
        break


print('Toto je koniec. Díky, že si si zahral.')
