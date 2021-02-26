#!/usr/bin/env python
from commands import *
import json


"""
+--------+
| heaven |
|        |
+--------+
    |
    |
    v
+-------+     +-------------+
|  hall |<--->| living room |
| t     |     | z           |
+-------+     +-------------+
    ^                                  N
    |                                  ^
    v                              W < o > E
+---------+                            v
| dungeon |                            S
| k, v    |
+---------+
"""

context = {
    'current_room': None,
    'backpack': [],
    'world': None,
    'line': None,
    'state': True,
    'history': []
}

# nacitanie sveta z json suboru
file = open('world.json', 'r', encoding='utf-8')
context['world'] = json.load(file)
file.close()

# game init
context['current_room'] = context['world']['chodba']


print(' _____                            ____                       ')
print('| ____|___  ___ __ _ _ __   ___  |  _ \ ___   ___  _ __ ___  ')
print("|  _| / __|/ __/ _` | '_ \ / _ \ | |_) / _ \ / _ \| '_ ` _ \ ")
print('| |___\__ \ (_| (_| | |_) |  __/ |  _ < (_) | (_) | | | | | |')
print('|_____|___/\___\__,_| .__/ \___| |_| \_\___/ \___/|_| |_| |_|')
print('                    |_|                                      ')
print('                                   (c)2021 Python 101 Version')
print()

show_room(context['current_room'])

while context['state'] == True:
    line = input('> ').strip().lower()
    context['line'] = line

    if line == 'o hre':
        cmd_about()

    elif line == 'prikazy':
        cmd_commands()

    elif line in ('vychod', 'v', 'east', 'e'):
        cmd_east(context)

    elif line in ('zapad', 'z', 'west', 'w'):
        cmd_west(context)

    elif line in ('juh', 'j', 'south'):
        context['history'].append('juh')
        cmd_south(context)

    elif line in ('sever', 's', 'north', 'n'):
        cmd_north(context)

    elif line == 'rozhliadni sa':
        cmd_look_around(context)

    elif line in ('inventar', 'i'):
        cmd_inventory(context)

    elif line.startswith('preskumaj'):
        cmd_explore(context)

    elif line.startswith('poloz'):
        cmd_drop(context)

    elif line.startswith('vezmi'):
        cmd_take(context)

    elif line.startswith('pouzi'):
        cmd_use(context)

    elif line in ('koniec', 'quit', 'exit', 'q', 'end', 'x'):
        context['state'] = False

    elif line == 'history':
        for item in context['history']:
            print(item)

    else:
        print("Tento príkaz nepoznám.")

    # vyhodnotenie, ci som hru skoncil
    if context['current_room']['name'] == 'sloboda':
        print(" _____                  _                 ")
        print("|  ___| __ ___  ___  __| | ___  _ __ ___  ")
        print("| |_ | '__/ _ \/ _ \/ _` |/ _ \| '_ ` _ \ ")
        print("|  _|| | |  __/  __/ (_| | (_) | | | | | |")
        print("|_|  |_|  \___|\___|\__,_|\___/|_| |_| |_|")
        print()
        print('A konečne si slobodný. Si sa kukol na prsteník, že fakt a fakt. Slobodaaaaaaaa.')
        break


print('Toto je koniec. Díky, že si si zahral.')
