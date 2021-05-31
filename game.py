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


STATE_EXIT = 1
STATE_PLAYING = 2


def find_item(name, context):
    items = context['room']['items'] + context['inventory']
    for item in items:
        if item['name'] == name:
            return item


def cmd_quit(context):
    print('Ta končíme')
    context['state'] = STATE_EXIT


def cmd_about(context):
    print('Room Escape')
    print('Táto mocná hra ťa naučí, ako prežiť v miestnosti uzavretej s Pythonom.')
    print('Created by šikovný mladý Pythonista (c)2021 mirek')
    print('Podporiť ho môžeš (aby bol ešte šikovnejší) na účte IBAN1234567890')


def cmd_drop(context):
    params = context['params']

    # step 1: neviem, co mam preskumat
    if len(params) == 0:
        print('Neviem, čo mám položiť.')
    else:
        # step 3: do miestnosti si polozil predmet {name}
        for item in context['inventory']:
            if item['name'] == params:
                context['inventory'].remove(item)
                context['room']['items'].append(item)
                print(f'Do miestnosti si vyložil predmet {item["name"]}.')
                break
        else:
            # step 2: taky predmet u seba nemas
            print('Taký predmet u seba nemáš.')


def cmd_take(context):
    params = context['params']
    room = context['room']
    inventory = context['inventory']
    inventory_capacity = context['inventory_capacity']

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
                    print(f'Do batohu si si vložil predmet {item["name"].lower()}.')
                else:
                    print('Batoh je plný')
                break

            elif item['name'] == params:
                print('Tento predmet sa nedá zobrať.')
                break
        else:
            # step 2: taky predmet u seba nemas
            print('Taký predmet tu nikde nevidím.')


def cmd_inspect(context):
    params = context['params']

    # step 1: neviem, co mam preskumat
    if len(params) == 0:
        print('Neviem, čo mám preskúmať.')
    else:
        item = find_item(params, context)

        if item is None:
            # step 2: Taky predmetu tu nikde nevidim
            print('Taký predmet tu nikde nevidím.')
        else:
            # step 3: {description}
            print(item['description'])


def cmd_inventory(context):
    if len(context['inventory']) == 0:
        print('Batoh je prázdny.')
        return

    print('V batohu máš:')
    for item in context['inventory']:
        print(f'\t{item["name"].lower()}')


def cmd_commands(context):
    print('Príkazy:')

    for cmd in context['commands']:
        print(f' {cmd["aliases"][0]} - {cmd["description"]}')


def cmd_look_around(context):
    show_room(context['room'])


def cmd_use(context):
    params = context['params']
    room = context['room']
    inventory = context['inventory']

    # step 1: neviem, co mam preskumat
    if len(params) == 0:
        print('Neviem, čo mám použiť.')
    else:
        # step 3: {description}
        for item in room['items'] + inventory:
            if item['name'] == params:
                if 'usable' in item['features']:

                    # pouzi kybel
                    if params == 'KYBEL':
                        # 1. zisti, ci dvere horia
                        door = find_item('HORIACE DVERE', context)
                        if door is None:
                            print('Ta neviem, čo by som s tým kýblom polial.')
                            break

                        # 2. polej dvere kyblom
                        print(
                            'Rozohnal si sa a celý obsah kýbla si vyšmaril na horiace dvere. Tie sa pod tlakom rozpadli a oheň sa zázrakom uhasil.')

                        # 3. aktualizuj stav vedra (prazdne vedro)
                        bucket = find_item('KYBEL', context)
                        bucket['name'] = 'PRAZDNY KYBEL'
                        bucket['description'] = 'Prázdny kýbel na 10l rozličného kvapalného obsahu.'

                        # 4. zmaz dvere
                        room['items'].remove(door)

                        # 5. pridaj vychod z miestnosti
                        room['exits'].append('sever')

                    # pouzitie novin
                    elif params == 'NOVINY':
                        print(
                            'Nove časy. Celkom hrube vydanie. Zo všetkých dvojstránok si úplne obložil dvere. Proste ti to prišlo ako celkom dobrý nápad.')
                        item['features'].remove('usable')
                        item['features'].remove('movable')
                        item['name'] = 'VYLEPENE NOVINY'
                        item['description'] = 'Nove casy. Jednotlivé stránky sú rozložené po celých dverách.'

                        if item in inventory:
                            inventory.remove(item)
                            room['items'].append(item)

                    # pouzitie zapaliek
                    elif params == 'ZAPALKY':
                        # 1. skontroluje, ci existuju vylepene noviny
                        for item in room['items']:
                            if item['name'] == 'VYLEPENE NOVINY':
                                newspaper = item
                                # 2. ak existuju, tak ich zapalime
                                print(
                                    'Zo zápalkovej krabičky si vytiahol jedinú zápalku, ktorá sa tam nachádzala a škrtol si ju. Priložil si ju k výtlačku Nových tajmsov a ten okamžite vzblkol. A spolu s ním aj celé dvere. Neviem, či toto bolo v tvojom pláne.')

                                # 3. zapalky zmiznu
                                matches = find_item('ZAPALKY', context)
                                if matches in inventory:
                                    inventory.remove(matches)
                                else:
                                    room['items'].remove(matches)

                                # 4. noviny zmiznu
                                if newspaper in inventory:
                                    inventory.remove(newspaper)
                                else:
                                    room['items'].remove(newspaper)

                                # 5. dvere sa zmenia na horiace dvere
                                door = find_item('DVERE', context)
                                door['name'] = 'HORIACE DVERE'
                                door['description'] = 'Dvere v plameňoch. Ani len priblížiť sa k nim nedá.'

                                break
                        else:
                            print(
                                'Mám tu len jednu zápalku. Nebudem ňou plytvať, keď nevieš čo chceš podpáliť.')

                else:
                    print('Tento predmet sa nedá použiť.')
                break
        else:
            # step 2: Taky predmetu tu nikde nevidim
            print('Taký predmet tu nikde nevidím.')


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
        'state': STATE_PLAYING,
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
    context['room'] = {
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

    context['commands'] = [
        {
            'description': 'Ukončí rozohratú hru.',
            'aliases': ('KONIEC', 'QUIT', 'EXIT', 'Q', 'BYE'),
            'exec': cmd_quit
        },

        {
            'description': 'Zobrazí informácie o hre',
            'aliases': ('O HRE', 'ABOUT', 'INFO'),
            'exec': cmd_about
        },

        {
            'description': 'Zobrazí informácie o zvolenom predmete.',
            'aliases': ('PRESKUMAJ', 'INSPECT'),
            'exec': cmd_inspect
        },

        {
            'description': 'Zobrazí zoznam príkazov dostupných v hre.',
            'aliases': ('PRIKAZY', 'COMMANDS', 'HELP', 'POMOC', '?'),
            'exec': cmd_commands
        },

        {
            'description': 'Zobrazí obsah hráčovho batohu.',
            'aliases': ('INVENTAR', 'INVENTORY', 'I'),
            'exec': cmd_inventory
        },

        {
            'description': 'Položí do miestnosti predmet z batohu.',
            'aliases': ('POLOZ', 'DROP'),
            'exec': cmd_drop
        },

        {
            'description': 'Vezme predmet z miestnosti a vloží ho do batohu.',
            'aliases': ('VEZMI', 'TAKE'),
            'exec': cmd_take
        },

        {
            'description': 'Použije zvolený predmet, ktorý sa môže nachádzať buď v batohu alebo v miestnosti',
            'aliases': ('POUZI', 'USE'),
            'exec': cmd_use
        },

        {
            'description': 'Vypíše opis miestnosti.',
            'aliases': ('ROZHLIADNI SA', 'LOOK AROUND', 'R'),
            'exec': cmd_look_around
        }
    ]

    # welcome
    print(' _____                            ____                       ')
    print('| ____|___  ___ __ _ _ __   ___  |  _ \ ___   ___  _ __ ___  ')
    print("|  _| / __|/ __/ _` | '_ \ / _ \ | |_) / _ \ / _ \| '_ ` _ \ ")
    print('| |___\__ \ (_| (_| | |_) |  __/ |  _ < (_) | (_) | | | | | |')
    print('|_____|___/\___\__,_| .__/ \___| |_| \_\___/ \___/|_| |_| |_|')
    print('                    |_|                     (c) mirek 2021   ')
    print()
    show_room(context['room'])

    # game loop
    while context['state'] == STATE_PLAYING:
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
