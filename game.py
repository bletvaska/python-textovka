#!/usr/bin/env python3
from world import world


def show_room(room):
    print(room['description'])
    print('Mozes ist na ', room['exits'])


current_room = 'pred jaskynou'

print("Indiana Jones")
show_room(world[current_room])

answer = None

while answer != 'koniec':
    answer = input('> ').strip().lower()

    if answer == 'rozhliadni sa':
        show_room(world[current_room])

    elif answer == 'o hre':
        print(
            'Ta tuto mocnu hru o Indianovi Jonesovi spachal uz nie az taky mlady fajny programator mirek v roku 2019. A ak ho chces podporit, ta mozes nejake fsimne poslat na ucet s IBANom SK1234567890987654321')

    elif answer == 'pomoc':
        print('ta pomoz si sam.')

    elif answer == 'prikazy':
        print('rozhliadni sa\no hre\npomoc\nprikazy')

    elif answer == 'koniec':
        print('ta diky ze si si zahral tuto mocnu hru, lebo je fakt mocna.')

    elif answer == 'vychod':
        room = world[current_room]

        if 'vychod' in room['exits']:
            current_room = room['exits']['vychod']
            show_room(world[current_room])
        else:
            print('tam sa neda ist')

    elif answer == 'zapad':
        room = world[current_room]

        if 'zapad' in room['exits']:
            current_room = room['exits']['zapad']
            show_room(world[current_room])
        else:
            print('tam sa neda ist')

    elif answer == 'sever':
        room = world[current_room]

        if 'sever' in room['exits']:
            current_room = room['exits']['sever']
            show_room(world[current_room])
        else:
            print('tam sa neda ist')

    elif answer == 'juh':
        room = world[current_room]

        if 'juh' in room['exits']:
            current_room = room['exits']['juh']
            show_room(world[current_room])
        else:
            print('tam sa neda ist')

    elif answer == 'dolu':
        room = world[current_room]

        if 'dolu' in room['exits']:
            current_room = room['exits']['dolu']
            show_room(world[current_room])
        else:
            print('tam sa neda ist')

    else:
        print('ta taky prikaz nepoznam')
