#!/usr/bin/env python3

# created by: mirek


def show_room(room):
    print(f'Nachádzaš sa v miestnosti {room["name"]}.')
    print(f'{room["description"]}')

    if len(room['items']) == 0:
        print('V miestnosti sa nenachadzaju ziadne predmety.')
    else:
        print(f'V miestnosti si nasiel tieto predmety:')
        for item in room['items']:
            print(f'\t* {item["name"].lower()}')

    if len(room['exits']) == 0:
        print('Z miestnosti neexistujú žiadne východy.')
    else:
        print(f'Východy z miestnosti: {room["exits"]}.')

STATE_EXIT = 1
STATE_PLAYING = 2


if __name__ == '__main__':
    # game initialization
    line = None
    game_state = STATE_PLAYING
    inventory_capacity = 2
    inventory = [
        {
            'name': 'ZAPALKY',
            'description': 'No zápalky. 4 kusy. Nepoužité. Krbové.',
            'features': ['movable', 'usable']
        }
    ]
    room = {
        'name': 'tmavá miestnosť',
        'description': 'Stojíš v tmavej miestnosti. Zrejme sa tu už dlho neupratovalo, lebo do nosa sa ti ftiera zepeklitý zápach niečoho zdochnutého. Ani len svetlo nepreniká cez zadebnené okná. I have a bad feeling about this place, ako by klasik povedal.',
        'exits': [],
        'items': [
            {
                'name': 'DVERE',
                'description': 'Velke masivne drevene dvere. Okrem toho su aj zamknute',
                'features': []
            },
            {
                'name': 'KYBEL',
                'description': 'Hrdzavý kýbel s obsahom bližšie nešpecifikovaným, ale zrejme to bude len voda.',
                'features': ['usable', 'movable']
            },
            {
                'name': 'NOVINY',
                'description': 'Staré suché Nové tajmsy z roku pána 1998. Z titulky rozpoznávaš len Vladimíra. To je teda veľký kus h... histórie.',
                'features': ['usable', 'movable']
            },
            {
                'name': 'NOZIK',
                'description': 'Síce zhrdzavený, ale stará klasika - nožík rybka.',
                'features': ['movable']
            },

        ]
    }

    # welcome
    print('Room Escape')
    show_room(room)

    # game loop
    while game_state == STATE_PLAYING:
        line = input('> ').upper().strip()

        if line in ('KONIEC', 'QUIT', 'EXIT', 'Q', 'BYE'):
            print('Ta končíme')
            game_state = STATE_EXIT

        elif line == 'O HRE':
            print('Room Escape')
            print('Táto mocná hra ťa naučí, ako prežiť v miestnosti uzavretej s Pythonom.')
            print('Created by šikovný mladý Pythonista (c)2021 mirek')
            print('Podporiť ho môžeš (aby bol ešte šikovnejší) na účte IBAN1234567890')

        elif line in ('ROZHLIADNI SA', 'LOOK AROUND', 'R'):
            show_room(room)

        elif line.split()[0] in ('POLOZ', 'DROP'):
            params = line.split()[1:]
            params = ' '.join(params)

            # step 1: neviem, co mam preskumat
            if len(params) == 0:
                print('Neviem, čo mám položiť.')
            else:
                # step 3: do miestnosti si polozil predmet {name}
                for item in inventory:
                    if item['name'] == params:
                        inventory.remove(item)
                        room['items'].append(item)
                        print(f'Do miestnosti si vyložil predmet {item["name"]}.')
                        break
                else:
                    # step 2: taky predmet u seba nemas
                    print('Taký predmet u seba nemáš.')

        elif line.split()[0] in ('VEZMI', 'TAKE'):
            params = line.split()[1:]
            params = ' '.join(params)

            # step 1: neviem, co mam vziat
            if len(params) == 0:
                print('Neviem, čo mám vziať.')
            else:
                # step 3: do inventára si vložil predmet {name}
                for item in room['items']:
                    if item['name'] == params and 'movable' in item['features']:
                        if len(inventory) < inventory_capacity:
                            room['items'].remove(item)
                            inventory.append(item)
                            print(f'Do batohu si si vložil predmet {item["name"]}.lower().')
                        else:
                            print('Batoh je plný')
                        break

                    elif item['name'] == params:
                        print('Tento predmet sa nedá zobrať.')
                        break
                else:
                    # step 2: taky predmet u seba nemas
                    print('Taký predmet tu nikde nevidím.')

        elif line.split()[0] in ('PRESKUMAJ', 'INSPECT'):
            params = line.split()[1:]
            params = ' '.join(params)

            # step 1: neviem, co mam preskumat
            if len(params) == 0:
                print('Neviem, čo mám preskúmať.')
            else:
                # step 3: {description}
                for item in room['items'] + inventory:
                    if item['name'] == params:
                        print(item['description'])
                        break
                else:
                    # step 2: Taky predmetu tu nikde nevidim
                    print('Taký predmet tu nikde nevidím.')

        elif line in ('INVENTAR', 'INVENTORY', 'I'):
            if len(inventory) == 0:
                print('Batoh je prázdny.')
            else:
                print('V batohu máš:')
                for item in inventory:
                    print(f'\t{item["name"].lower()}')

        elif line in ('PRIKAZY', 'COMMANDS', 'HELP', 'POMOC', '?'):
            print(
                f'Príkazy:\n KONIEC - Ukonci hru\n PRIKAZY - Vypise zoznam prikazov\n ROZHLIADNI SA - Vypíše opis miestnosti\n O HRE - Zakladne informacie o hre')

        else:
            print('Taký príkaz nepoznám.')

    print('Created by (c)2021 mirek')
