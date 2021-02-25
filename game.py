#!/usr/bin/env python
import json


def show_room(room):
    # nazov a opis miestnosti
    print(f'Nachádzaš sa v miestnosti {room["name"]}.')
    print(room['description'])

    # vypis vychodov z miestnosti
    if room['exits']['east'] == None and room['exits']['west'] == None and room['exits']['south'] == None and room['exits']['north'] == None:
        print('Z miestnosti neexistujú žiadne východy.')
    else:
        print('Možné východy z miestnosti:')
        if room['exits']['east'] != None:
            print('  vychod')
        if room['exits']['west'] != None:
            print('  zapad')
        if room['exits']['south'] != None:
            print('  juh')
        if room['exits']['north'] != None:
            print('  sever')

    # vypis predmetov v miestnosti
    if len(room['items']) == 0:
        print('Nevidíš tu nič zaujímavé.')
    else:
        print('Vidíš:')
        for item in room['items']:
            print(f'  {item["name"]}')


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
    'features': ['movable', ]
}

dvere = {
    'name': 'vchodove dvere',
    'description': 'Masívne oceľové vchodové dvere s dvoma zámkami. Toto asi nebude len tak obyčaný bytík nejakého študentíka.',
    'features': []
}

world['chodba']['items'].append(dvere)

# world['chodba']['items'].append(teplaky)
# world['chodba']['items'].append(kanister)


# game init
current_room = world['chodba']
backpack = []
backpack.append(kanister)
backpack.append(teplaky)


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
        name = current_room['exits']['east']
        if name != None:
            current_room = world[name]
            show_room(current_room)
        else:
            print('Tam sa nedá ísť.')

    elif line == 'zapad':
        name = current_room['exits']['west']
        if name != None:
            current_room = world[name]
            show_room(current_room)
        else:
            print('Tam sa nedá ísť.')

    elif line == 'juh':
        name = current_room['exits']['south']
        if name != None:
            current_room = world[name]
            show_room(current_room)
        else:
            print('Tam sa nedá ísť.')

    elif line == 'sever':
        name = current_room['exits']['north']
        if name != None:
            current_room = world[name]
            show_room(current_room)
        else:
            print('Tam sa nedá ísť.')

    elif line == 'rozhliadni sa':
        show_room(current_room)

    elif line == 'inventar':
        if len(backpack) == 0:
            print('Batoh je prázdny.')
        else:
            print('V batohu máš:')
            for item in backpack:
                print(f'  {item["name"]}')

    elif line.startswith('preskumaj'):
        cmd = line.split(maxsplit=1)
        if len(cmd) == 1:
            print('Čo chceš preskúmať?')
        else:
            name = cmd[1]

            found = False
            for item in current_room['items']:
                if item['name'] == name:
                    print(item['description'])
                    found = True
                    break

            if found == False:
                print('Taký predmet tu nikde nevidím.')

    elif line.startswith('poloz'):
        cmd = line.split(maxsplit=1)
        if len(cmd) == 1:
            print('Neviem, čo chceš položiť.')
        else:
            name = cmd[1]
            found = False
            for item in backpack:
                if item['name'] == name:
                    backpack.remove(item)
                    current_room['items'].append(item)
                    print(f'Do miestnosti si položil {item["name"]}.')
                    found = True
                    break
            if found == False:
                print('Taký predmet u seba nemáš.')

    elif line.startswith('vezmi'):
        cmd = line.split(maxsplit=1)
        if len(cmd) == 1:
            print('Neviem, čo chceš zobrať.')
        else:
            name = cmd[1]
            found = False
            for item in current_room['items']:

                if item['name'] == name:
                    if 'movable' in item['features']:
                        current_room['items'].remove(item)
                        backpack.append(item)
                        print(f'Do batohu si vložil {item["name"]}.')
                    else:
                        print('Tento predmet sa nedá zobrať.')

                    found = True
                    break

            if found == False:
                print(
                    f'Taký predmet v miestnosti {current_room["name"]} nevidím.')

    else:
        print("Tento príkaz nepoznám.")

print('Toto je koniec. Díky, že si si zahral.')
