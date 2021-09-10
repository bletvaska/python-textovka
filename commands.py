import random

import features
import states

_zen_of_python = [
    'Beautiful is better than ugly.',
    'Explicit is better than implicit.',
    'Simple is better than complex.',
    'Complex is better than complicated.',
    'Flat is better than nested.',
    'Sparse is better than dense.',
    'Readability counts.',
    "Special cases aren't special enough to break the rules.",
    'Although practicality beats purity.',
    'Errors should never pass silently.',
    'Unless explicitly silenced.',
    'In the face of ambiguity, refuse the temptation to guess.',
    'There should be one-- and preferably only one --obvious way to do it.',
    "Although that way may not be obvious at first unless you're Dutch.",
    'Now is better than never.',
    'Although never is often better than *right* now.',
    "If the implementation is hard to explain, it's a bad idea.",
    'If the implementation is easy to explain, it may be a good idea.',
    "Namespaces are one honking great idea -- let's do more of those!",
]


def inventory(name: str, context: dict) -> None:
    if len(context['inventory']) == 0:
        print('Batoh je prázdny.')
    else:
        print('V batohu máš:')
        for item in context['inventory']:
            print(f'\t* {item["name"]}')


def look_around(name: str, context: dict) -> None:
    room = context['room']
    print(f'Nachádzaš sa v miestnosti {room["name"]}.')
    print(f'{room["description"]}')

    if len(room['items']) == 0:
        print('Nevidíš tu nič zaujímavé.')
    else:
        print(f'Vidíš:')
        for item in room['items']:
            print(f'\t* {item["name"]}')


def drop(name: str, context: dict) -> None:
    if name == '':
        print('Neviem, aký predmet chceš položiť.')
    else:
        for item in context['inventory']:
            if item['name'] == name:
                # vybrat ho z inventaru
                context['inventory'].remove(item)

                # polozit ho do miestnosti
                context['room']['items'].append(item)

                print(f'Predmet {name} si vyložil do miestnosti.')
                break
        else:
            print('Taký predmet u seba nemáš.')


def take(name: str, context: dict) -> None:
    """
    Represents the TAKE command.

    :param name: the name of item do describe
    :param room: the room object, where the player is currently in
    :param inventory: the player's inventory
    """

    room = context['room']
    inventory = context['inventory']

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


def examine(name: str, context: dict) -> None:
    """
    Represents the examine command.

    :param name: the name of item do describe
    :param room: the room object, where the player is currently in
    :param inventory: the player's inventory
    """

    room = context['room']
    inventory = context['inventory']

    if len(name) == 0:
        print('Neviem, aký predmet chceš preskúmať.')
    else:
        for item in room['items'] + inventory:
            if item['name'] == name:
                print(item['description'])
                break
        else:
            print('Taký predmet tu nigde nevidím.')


def use(name: str, context: dict) -> None:
    """
    Represents the examine command.

    :param name: the name of item do describe
    :param context: the game context
    """

    room = context['room']
    inventory = context['inventory']

    if len(name) == 0:
        print('Neviem, aký predmet chceš použiť.')
    else:
        for item in room['items'] + inventory:
            if item['name'] == name:
                if features.USABLE not in item['features']:
                    print('Tento predmet sa nedá použiť.')
                else:

                    if name == 'ucebnica jazyka python':
                        print('Zalistoval si v učebnici a dočítal si sa, že:')
                        print(random.choice(_zen_of_python))

                    elif name == 'kanister':
                        # aktualizovali sme kanister
                        item['description'] = 'Prázdny kanister. Po pričuchnutí je ti to jasné - bol tu benzín.'
                        item['features'].remove(features.USABLE)

                        # aktualizujeme dvere
                        for it in room['items']:
                            if it['name'] == 'dvere' and it['state'] == 'zamknute':
                                it['state'] = 'poliate'
                                it['description'] = 'Dvere. Stále zamknuté, ale ako bonus sú poliate benzínom. Je ti jasné, kto za to môže.'
                                break

                        # a akcia
                        print('Ta som odšroboval, rozohnal som sa a celý obsah kanistra som vylial na dvere. V '
                              'miestnosti sa náhle rozľahol benzínový zápach. Proste vysoko-oktánová fajnotka.')

                    elif name == 'zapalky':
                        # musim byt v miestnosti s dverami, ktore su poliate benzinom!!!
                        door = None
                        for it in room['items']:
                            if it['name'] == 'dvere' and it['state'] == 'poliate':
                                door = it

                                # zmazeme/vyhodime zapalky z hry (bud z miestnosti alebo z batohu)
                                if item in room['items']:
                                    room['items'].remove(item)
                                else:
                                    inventory.remove(item)

                                # co sa stane s dverami:
                                door['state'] = 'horiace'
                                # zmena opisu
                                door['description'] = 'Doteraz tie dvere iba voňali, teraz už aj horia. Zaujímavé, čo všetko sa dnes deje v tom svete.'
                                # nazov: horiace dvere
                                door['name'] = 'horiace dvere'

                                # akcia
                                print('Zahrkal si krabičkou zápaliek a jednu si z nej vytiahol. Nadýchol si sa, škrtol si a ona chytila. Usmial si sa a s úsmevom na tvári si horiacu zápalku voľne pohodil smerom k dverám. Tie neváhali a okamžite zbĺkli. Ten benzín urobil svoje.')
                                break
                        else:
                            print('Krabička zápaliek. Nič zaujímavé. Len na čo by som ich tak použil?')

                        # todo: zapalky chytia az na tretikrat/posledna zapalka

                    elif name == 'hasiaci pristroj':
                        # musia horiet dvere
                        door = None
                        for it in room['items']:
                            if it['name'] == 'horiace dvere':
                                # zmiznu dvere z miestnosti
                                room['items'].remove(it)

                                # hasiaci pristroj bude nepouzitelny
                                item['features'].remove(features.USABLE)

                                # zmenim mu opis na prazdny hasiaci pristroj
                                item['description'] = 'Ručný hasiaci prístroj prázdny. Značka - červený.'

                                # akcia
                                print('Zahasil si dvere. Tie sa vplyvom tlaku hasiacej zmesy rozpadli a uvoľnili ti východ z miestnosti.')
                                break
                        else:
                            print('Aj by som nasnežil, ale nie je na čo.')

                    else:
                        print(f'Snažím sa použiť predmet {name}')
                return
        else:
            print('Taký predmet tu nikde nevidím.')


def about(name: str, context: dict) -> None:
    print('Hru spáchal v (c) 2021 mirek.')
    print('Ďalšie dobrodužstvo Indiana Jonesa. Tentokrát sa pokúsi o únik zo skladu Košického Technického múzea.')


def quit_game(name: str, context: dict) -> None:
    print('ta koncime')
    context['state'] = states.QUIT


def show_commands(name: str, context: dict) -> None:
    print('Zoznam príkazov hry:')

    for command in context['commands']:
        print(f'\t* {command["name"]} - {command["description"]}')


commands = [
    {
        'name': 'preskumaj',
        'aliases': ('examine',),
        'exec': examine,
        'description': 'zobrazí informácie o zvolenom predmete'
    },

    {
        'name': 'poloz',
        'aliases': ('drop',),
        'exec': drop,
        'description': 'vyberie predmet z batohu a položí ho do miestnosti'
    },

    {
        'name': 'koniec',
        'aliases': ('quit', 'bye', 'q', 'ukoncit'),
        'description': 'ukončí rozohratú hru',
        'exec': quit_game
    },

    {
        'name': 'o hre',
        'aliases': ('about',),
        'description': 'zobrazí informácie o hre',
        'exec': about
    },

    {
        'name': 'rozhliadni sa',
        'aliases': ('look around',),
        'description': 'zobrazí obsah miestnosti',
        'exec': look_around
    },

    {
        'name': 'inventar',
        'aliases': ('inventory', 'i'),
        'description': 'zobrazí obsah batohu',
        'exec': inventory
    },

    {
        'name': 'vezmi',
        'aliases': ('take',),
        'description': 'vezme predmet z miestnosti a vloží ho do batohu',
        'exec': take
    },

    {
        'name': 'prikazy',
        'aliases': ('commands', 'help', 'pomoc'),
        'description': 'zobrazí zoznam príkazov dostupných v hre',
        'exec': None  # commands
    },

    {
        'name': 'pouzi',
        'aliases': ('pouzit', 'use'),
        'description': 'použije zvolený predmet',
        'exec': use
    }
]
