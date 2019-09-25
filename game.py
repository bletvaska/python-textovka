#!/usr/bin/env python3

world = {
    'pred jaskynou': {
        'name': 'pred jaskynou',
        'description': "Stojis pred vchodom do tajomnej jaskyne. Jaskyna nevesti nic dobre.",
        'exits': 'vychod'
    },

    'v jaskyni': {
        'name': 'v jaskyni',
        'description': 'Stojis v temnej jaskyni. Uz aj tak mizernu viditelnost znizuju este pavuciny, ktorych je tu teda riadna kopa.',
        'exits': 'zapad'
    }
}

current_room = 'pred jaskynou'

print("Indiana Jones")

print(world[current_room]['description'])
print('Mozes ist na ', world[current_room]['exits'])


answer = None

while answer != 'koniec':
    answer = input('> ').strip().lower()

    if answer == 'rozhliadni sa':
        print(world[current_room]['description'])
        print('Mozes ist na ', world[current_room]['exits'])

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
        current_room = 'v jaskyni'
        print(world[current_room]['description'])
        print('Mozes ist na ', world[current_room]['exits'])

    else:
        print('ta taky prikaz nepoznam')
