#!/usr/bin/env python3

import features
import states


def look_around(room: dict):
    print(f'Nachádzaš sa v miestnosti {room["name"]}.')
    print(f'{room["description"]}')

    if len(room['items']) == 0:
        print('Nevidíš tu nič zaujímavé.')
    else:
        print(f'Vidíš:')
        for item in room['items']:
            print(f'\t* {item["name"]}')


def drop(name: str, room: dict, inventory: list) -> None:
    if name == '':
        print('Neviem, aký predmet chceš položiť.')
    else:
        for item in inventory:
            if item['name'] == name:
                # vybrat ho z inventaru
                inventory.remove(item)

                # polozit ho do miestnosti
                room['items'].append(item)

                print(f'Predmet {name} si vyložil do miestnosti.')
                break
        else:
            print('Taký predmet u seba nemáš.')


def take(name: str, room: dict, inventory: list) -> None:
    """
    Represents the TAKE command.

    :param name: the name of item do describe
    :param room: the room object, where the player is currently in
    :param inventory: the player's inventory
    """

    if name == '':
        print('Neviem, aký predmet chceš vziať.')
    else:
        for item in room['items']:
            if item['name'] == name:
                # overit, ci je batoh plny
                # todo: zmeni konstantu na premennu
                if len(inventory) >= 2:
                    print('Batoh je plný.')

                # overit, ci sa da zobrat
                elif features.MOVABLE in item['features']:
                    # vybrat ho z roomu
                    room['items'].remove(item)

                    # vlozit do batohu
                    inventory.append(item)

                    print(f'Predmet {name} si si vložil do batohu.')
                else:
                    print('Tento predmet sa nedá zobrať.')

                break
        else:
            print('Taký predmet tu nikde nevidím.')


def examine(name: str, room: dict, inventory: list) -> None:
    """
    Represents the examine command.

    :param name: the name of item do describe
    :param room: the room object, where the player is currently in
    :param inventory: the player's inventory
    """

    for item in room['items'] + inventory:
        if item['name'] == name:
            print(item['description'])
            break
    else:
        print('Taký predmet tu nigde nevidím.')


def main():
    room = {
        'name': 'dungeon',
        'description': 'Nachádzaš sa v tmavej miestnosti. Každé okno je zvonku zabarikádované a do miestnosti preniká len '
                       'úzky prameň svetla. Masívne drevené dvere sú jediným východom z miestnosti.',
        'items': [
            {
                'name': 'kybel',
                'description': 'Kýbel plný vody.',
                'features': [features.MOVABLE, features.USABLE]
            },

            {
                'name': 'hasiaci pristroj',
                'description': 'Ručný hasiaci prístroj plný. Značka - červený.',
                'features': [features.MOVABLE, features.USABLE]
            },

            {
                'name': 'zapalky',
                'description': 'Krabička zápaliek vyrobená ešte v Československu. Kvalitka.',
                'features': [features.MOVABLE, features.USABLE]
            },

            {
                'name': 'dvere',
                'description': 'Veľké masívne drevené dvere. Zamknuté.',
                'features': []
            }
        ]
    }

    line = None
    state = states.PLAYING
    inventory = [
        {
            'name': 'ucebnica jazyka python',
            'description': 'Mocná učebnica jazyka Python od známeho Pytonistu Jana.',
            'features': [features.MOVABLE, features.USABLE]
        }
    ]

    look_around(room)

    while state == states.PLAYING:
        line = input('> ').strip().lower()

        if line == 'o hre':
            print('Hru spáchal v (c) 2021 mirek.')
            print(
                'Ďalšie dobrodužstvo Indiana Jonesa. Tentokrát sa pokúsi o únik zo skladu Košického Technického múzea.')

        elif line == 'prikazy':
            print('Zoznam príkazov hry:')

            print('* koniec - ukončí rozohratú hru')
            print('* o hre - zobrazí informácie o hre')
            print('* poloz - vyberie predmet z batohu a položí ho do miestnosti')
            print('* preskumaj - zobrazí informácie o zvolenom predmete')
            print('* prikazy - zobrazí zoznam príkazov dostupných v hre')
            print('* rozhliadni sa - zobrazí obsah miestnosti')
            print('* inventar - zobrazí obsah batohu')
            print('* vezmi - vezme predmet z miestnosti a vloží ho do batohu')

        elif line in ('koniec', 'quit', 'bye', 'q', 'ukoncit'):
            print('ta koncime')
            state = states.QUIT

        elif line == 'rozhliadni sa':
            look_around(room)

        elif line in ('inventar', 'inventory', 'i'):
            if len(inventory) == 0:
                print('Batoh je prázdny.')
            else:
                print('V batohu máš:')
                for item in inventory:
                    print(f'\t* {item["name"]}')

        elif line.startswith('preskumaj'):
            name = line.split('preskumaj')[1].strip()

            if len(name) == 0:
                print('Neviem, aký predmet chceš preskúmať.')
            else:
                examine(name, room, inventory)

        elif line.startswith('vezmi'):
            name = line.split('vezmi')[1].strip()
            take(name, room, inventory)

        elif line.startswith('poloz'):
            name = line.split('poloz')[1].strip()
            drop(name, room, inventory)

        else:
            print('Taký príkaz nepoznám.')

    print('...koniec...')


if __name__ == '__main__':
    main()
