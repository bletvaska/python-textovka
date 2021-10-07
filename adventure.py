#!/usr/bin/env python3

# premenne definujuce rozny stav hry
STATE_QUIT = 1
STATE_PLAYING = 2
STATE_DEATH = 3


def cmd_look_around(room: dict):
    """
    Prints description about the room

    Prints out the description about the room given as parameter.
    :param room: room to describe
    """
    print(f'Nachádzaš sa v miestnosti {room["name"]}')
    print(room['description'])

    # print items in the room
    if room['items'] == []:  # len(room['items'] == 0
        print('Nevidíš tu nič zvláštne.')
    else:
        print("Vidíš:")
        for item in room['items']:
            print(f'\t* {item}')


def cmd_commands():
    print('Dostupné príkazy v hre:')
    print('* o hre - zobrazí informácie o hre')
    print('* rozhliadni sa - zobrazí opis miestnosti, v ktorej sa hráč aktuálne nachádza')
    print('* prikazy - zobrazí zoznam dostupných príkazov v hre')
    print('* koniec - ukončí hru')


def cmd_about():
    print('Indiana Jones a jeho Pythoňácke dobrodružstvo')
    print('Nestarnúci hrdina Indiana Jones sa tentokrát ocitol sám pustý v škaredej miestnosti. A jedine '
          'Pythoňácky programátori mu môžu zachrániť krk. Je to na tebe.')
    print('\n(c) 2021 hru spáchal mirek')


line = None
game_state = STATE_PLAYING
room = {
    'name': 'dungeon',
    'description': 'Nachádzaš sa v tmavej miestnosti, kde sa po stenách nachádzajú hieroglify z obdobia Juraja Jánošíka. Valaška a krpce sú najščastejším motívom, ktorý vidíš na vyrytých postavách na stene. Stiesňujúce miesto.',
    'items': [
        {
            'name': 'noviny',
            'description': 'dennik sme s autorskou strankou sama marca',
            'features': ['movable', 'usable'],
        },

        {
            'name': 'vedro',
            'description': 'Vedro plné vody.',
            'features': ['movable', 'usable']
        },

        {
            'name': 'zapalky',
            'description': 'Krabička so zápalkami.',
            'features': ['movable', 'usable']
        },

        {
            'name': 'kanister',
            'description': 'Vysokooktánový benzín tvorí obsah tohto kanistra. Kvalitka za rozumnú cenu.',
            'features': ['usable', 'movable']
        },

        {
            'name': 'dvere',
            'description': 'Masívne dubové dvere. Zamknuté.',
            'features': []
        }
    ],
    'exits': []
}

# game intro
print('Indiana Jones')
print('alebo veľké Pythoňácke dobrodružstvo')
cmd_look_around(room)

# game loop
while game_state == STATE_PLAYING:
    line = input('> ').lstrip().rstrip().lower()

    if len(line) == 0:  # line == ''
        continue

    elif line in ('o hre', 'about'):
        cmd_about()

    elif line in ('rozhliadni sa', 'look around'):
        cmd_look_around(room)

    elif line in ('prikazy', 'commands', 'help', '?'):
        cmd_commands()

    elif line in ('koniec', 'quit', 'exit', 'q'):
        game_state = STATE_QUIT

    else:
        print('Tento príkaz nepoznám.')

print('Končíme.')
