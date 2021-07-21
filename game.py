#!/usr/bin/env python3

def cmd_drop(line: str, room: dict, backpack: dict):
    name = line[5:].strip()

    if name == '':
        print('Neviem, čo chceš položiť.')

    else:
        for item in backpack['items']:
            if item['name'] == name:
                backpack['items'].remove(item)
                room['items'].append(item)
                print(f'Do miestnosti si položil predmet {name}.')
                break

        # if no such item was found
        else:
            print('Taký predmet tu nigde nevidím.')


def cmd_take(line: str, room: dict, backpack: dict):
    name = line[5:].strip()

    if len(backpack['items']) >= backpack['capacity']:
        print('Batoh je plný.')

    elif name == '':
        print('Neviem, čo chceš zobrať.')

    else:
        for item in room['items']:
            if item['name'] == name:
                backpack['items'].append(item)
                room['items'].remove(item)
                print(f'Predmet {name} si si vložil do batohu.')
                break

        # if no such item was found
        else:
            print('Taký predmet tu nigde nevidím.')


def cmd_explore(line: str, room: dict, backpack: dict):
    name = line[9:].strip()

    # if no name was given
    if name == '':
        print('Neviem, čo chceš preskúmať.')

    else:
        for item in room['items'] + backpack['items']:
            # if name was found
            if item['name'] == name:
                print(item['description'])
                break
        # if no such item was found
        else:
            print('Taký predmet tu nigde nevidím.')


def cmd_inventory(backpack: dict):
    if backpack['items'] == []:
        print('Batoh je prázdny.')
    else:
        print('V batohu máš:')
        for item in backpack['items']:
            print(f'\t{item["name"]}')


def cmd_commands():
    print('Dostupné príkazy v hre:')
    print('* inventar - zobrazí obsah batohu')
    print('* koniec - ukončí rozohratú hru')
    print(
        '* o hre - zobrazí informácie o fantastickom autorovi hry a o hre samotnej')
    print('* preskumaj - preskúma zadaný predmet')
    print('* prikazy - zobrazí zoznam príkazov, ktoré hra podporuje')
    print('* rozhliadni sa - zobrazí opis miestnosti, v ktorej sa hráč nachádza')
    print('* vezmi - vezmi zadaný predmet z miestnosti a vloží si ho do batohu')
    print()


def cmd_about():
    print('Hru spáchal  (c)2021 mirek')
    print('Ďalší príbeh Indiana Jonesa sa odohráva v temnej komôrke.')
    print()


def show_room(room: dict):
    """
    Prints room on the screen.

    Prints out the room given as the parameter of type dictionary on the screen.

    :params room: the room to show
    """
    if type(room) is not dict:
        raise TypeError('Room is not of type dictionary.')

    print(f'Nachádzaš sa v miestnosti {room["name"]}')
    print(room['description'])

    # print items in the room
    if room['items'] == []:
        print('Nevidíš tu nič zvláštne.')
    else:
        print('Vidíš: ')
        for item in room['items']:
            print(f'\t{item["name"]}')

    # print exits from the room
    if room['exits'] == []:
        print('Z tejto miestnosti neexistujú žiadne východy.')

    print()


if __name__ == '__main__':
    print(' ___           _ _                         _                       ')
    print('|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ')
    print(" | || '_ \ / _` | |/ _` | '_ \ / _` |  _  | |/ _ \| '_ \ / _ \/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\__ \\")
    print('|___|_| |_|\__,_|_|\__,_|_| |_|\__,_|  \___/ \___/|_| |_|\___||___/')

    print('                                                     (c) 2021 mirek')

    backpack = {
        'capacity': 2,
        'items': [
            {
                'name': 'noviny',
                'description': 'Nové tajmsy, husté čítanie na každý deň.',
                'features': ['movable']
            }
        ]
    }

    room = {
        'description': 'Nachádzaš v tmavej miestnosti. Kamenné múry dávajú tušiť, že sa nachádzaš v nejakej kamennej kobke. Žeby podzemie hradu v Grunwalde? Okná tu nie sú žiadne, čo by ťa uistili o správnosti tohto predpokladu.',
        'name': 'kobka',
        'items': [
            {
                'name': 'vedro',
                'description': 'Vedro plné vody.',
                'features': ['movable']
            },
            {
                'name': 'kanister',
                'description': 'Kanister plný benzínu.',
                'features': ['movable']
            },
            {
                'name': 'zapalky',
                'description': 'Zápalky na vatru.',
                'features': ['movable']

            },
            {
                'name': 'chladnicka',
                'description': 'Chladnička značky Calex. Zvláštne znamenie: pokazená.',
                'features': []
            }
        ],
        'exits': []
    }

    show_room(room)

    line = None

    # input parser
    while line != 'koniec':
        line = input('> ').rstrip().lstrip().lower()

        if line == 'o hre':
            cmd_about()

        elif line == 'rozhliadni sa':
            show_room(room)

        elif line == 'prikazy':
            cmd_commands()

        elif line == 'inventar':
            cmd_inventory(backpack)

        elif line.startswith('preskumaj'):
            cmd_explore(line, room, backpack)

        elif line.startswith('vezmi'):
            cmd_take(line, room, backpack)

        elif line.startswith('poloz'):
            cmd_drop(line, room, backpack)

        elif line in ('koniec', ''):
            continue

        else:
            print('Taký príkaz nepoznám.')
