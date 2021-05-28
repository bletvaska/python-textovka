#!/usr/bin/env python3

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


if __name__ == '__main__':
    # game initialization
    line = None
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
    while line != 'KONIEC':
        line = input('> ').upper().strip()

        if line == 'KONIEC':
            print('Ta končíme')
            # pass

        elif line == 'O HRE':
            print('Room Escape')
            print('Táto mocná hra ťa naučí, ako prežiť v miestnosti uzavretej s Pythonom.')
            print('Created by šikovný mladý Pythonista (c)2021 mirek')
            print('Podporiť ho môžeš (aby bol ešte šikovnejší) na účte IBAN1234567890')

        elif line == 'ROZHLIADNI SA':
            show_room(room)

        elif line.split()[0] == 'POLOZ':
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

        elif line.split()[0] == 'VEZMI':
            params = line.split()[1:]
            params = ' '.join(params)

            # step 1: neviem, co mam vziat
            if len(params) == 0:
                print('Neviem, čo mám vziať.')
            else:
                # step 3: do inventára si vložil predmet {name}
                for item in room['items']:
                    if item['name'] == params:
                        if 'movable' in item['features']:
                            room['items'].remove(item)
                            inventory.append(item)
                            print(f'Do batohu si si vložil predmet {item["name"]}.')
                        else:
                            print('Tento predmet sa nedá zobrať.')
                        break
                else:
                    # step 2: taky predmet u seba nemas
                    print('Taký predmet tu nikde nevidím.')

        elif line.split()[0] == 'PRESKUMAJ':
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

        elif line == 'INVENTAR':
            if len(inventory) == 0:
                print('Batoh je prázdny.')
            else:
                print('V batohu máš:')
                for item in inventory:
                    print(f'\t{item["name"].lower()}')

        elif line == 'PRIKAZY':
            print(
                f'Príkazy:\n KONIEC - Ukonci hru\n PRIKAZY - Vypise zoznam prikazov\n ROZHLIADNI SA - Vypíše opis miestnosti\n O HRE - Zakladne informacie o hre')

        else:
            print('Taký príkaz nepoznám.')

    print('Created by (c)2021 mirek')
