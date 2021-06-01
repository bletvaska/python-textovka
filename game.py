#!/usr/bin/env python3

from commands import commands as list_of_commands
from helper import show_room
import states


def parse(context, line):
    for cmd in context['commands']:
        for alias in cmd['aliases']:
            if line.startswith(alias):
                context['params'] = line.replace(alias, '').strip()
                return cmd

    return None


def main():
    # game initialization
    context = {
        'state': states.STATE_PLAYING,
        'inventory': [],
        'inventory_capacity': 2,
        'room': None
    }

    context['inventory'].append({
        'name': 'ZAPALKY',
        'description': 'No zápalky. 4 kusy. Nepoužité. Krbové.',
        'features': ['movable', 'usable']
    })

    line = None
    context['room'] = 'tmavá miestnosť'

    context['world'] = {
        'jama': {
            'name': 'jama',
            'description': 'Kde sa tu len vzala? 2x2 metre, ale do výšky hádam 3 metre.',
            'exits': {},
            'items': []
        },

        'spálňa': {
            'name': 'spálňa',
            'description': 'Vyzerá to ako spálňa, až na to, že tu chýba posteľ, nočné stolíky, lampa a skriňa. Ale záclony sú také... ako do spálne.',
            'exits': {
                'west': 'tmavá miestnosť'
            },
            'items': [
                {
                    'name': 'NOVINY',
                    'description': 'Staré suché Nové tajmsy z roku pána 1998. Z titulky rozpoznávaš len Vladimíra. To je teda veľký kus h... histórie.',
                    'features': ['usable', 'movable']
                }
            ]
        },

        'kuchyňa': {
            'name': 'kuchyňa',
            'description': 'Dve platničky, šparhét a chladnička Calex. Hrnčeky, lyžičky, nožíky. Podľa pachu sa tu naposledy varili ryby. Alebo to je syr? Ponožky?',
            'exits': {
                'south': 'tmavá miestnosť'
            },
            'items': [
                {
                    'name': 'NOZIK',
                    'description': 'Síce zhrdzavený, ale stará klasika - nožík rybka.',
                    'features': ['movable']
                },

                {
                    'name': 'KYBEL',
                    'description': 'Hrdzavý kýbel s obsahom bližšie nešpecifikovaným, ale zrejme to bude len voda.',
                    'features': ['usable', 'movable']
                },
            ]

        },

        'záhradka': {
            'name': 'záhradka',
            'description': 'Značne neudržiavaná záhradka nevšedných rozmerov.',
            'exits': {
                'east': 'tmavá miestnosť'
            },
            'items': []
        },

        'tmavá miestnosť': {
            'name': 'tmavá miestnosť',
            'description': 'Stojíš v tmavej miestnosti. Zrejme sa tu už dlho neupratovalo, lebo do nosa sa ti ftiera zepeklitý zápach niečoho zdochnutého. Ani len svetlo nepreniká cez zadebnené okná. I have a bad feeling about this place, ako by klasik povedal.',
            'exits': {
                'south': 'jama',
                'north': 'kuchyňa',
                'east': 'spálňa'
            },
            'items': [
                {
                    'name': 'DVERE',
                    'description': 'Velke masivne drevene dvere. Okrem toho su aj zamknute',
                    'features': []
                }

            ]
        }
    }

    context['commands'] = list_of_commands

    # welcome
    print(' _____                            ____                       ')
    print('| ____|___  ___ __ _ _ __   ___  |  _ \ ___   ___  _ __ ___  ')
    print("|  _| / __|/ __/ _` | '_ \ / _ \ | |_) / _ \ / _ \| '_ ` _ \ ")
    print('| |___\__ \ (_| (_| | |_) |  __/ |  _ < (_) | (_) | | | | | |')
    print('|_____|___/\___\__,_| .__/ \___| |_| \_\___/ \___/|_| |_| |_|')
    print('                    |_|                     (c) mirek 2021   ')
    print()

    room_name = context['room']
    room = context['world'][room_name]
    show_room(room)

    # game loop
    while context['state'] == states.STATE_PLAYING:
        # parsovanie vstupu
        line = input('> ').upper().strip()

        cmd = parse(context, line)
        if cmd is None:
            print('Taký príkaz nepoznám.')
        else:
            cmd['exec'](context)

    print('Created by (c)2021 mirek')


if __name__ == '__main__':
    main()
