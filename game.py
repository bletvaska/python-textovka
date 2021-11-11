#!/usr/bin/env python3
import states
from typing import Dict


def show_room(room: Dict):
    """
    Show content of the room.
    The function shows name and description of the room. It also prints the list of items, which are in the room, or
    the information about there are no items in the room. Finally, it prints out also list of available exits from the
    room or special string, when there is no exit from the room.
    :param room: the room to print info about
    """
    # type checking
    if type(room) is not dict:
        raise TypeError('Room is not of type dictionary.')

    print(f'Nachádzaš sa v miestnosti {room["name"]}.')
    print(f'{room["description"]}')

    if room["exits"] == []:
        print("Z tejto miestnosti nevedú žiadne východy.")

    if room["items"] == []:
        print("Nevidíš tu nič zvláštne.")
    else:
        print(f"Vidíš: {', '.join(room['items'])}")
        # for item in room['items']:
        #     print(f"* {item}")

    # return None


if __name__ == '__main__':
    # init game
    game_state = states.PLAYING
    room = {
        'name': 'dungeon',
        'description': 'Nachádzaš sa v tmavej zatuchnutej miestnosti. Na kamenných stenách sa nenachádza žiadne okno, '
                       'čo dáva tušiť, že si niekoľko metrov pod zemou. Žeby košický hrad? Aj to je možné, ti prebleslo '
                       'hlavou.',
        'items': ['kanister', 'zapalky', 'hasiaci pristroj', 'noviny'],
        'exits': []
    }

    # banner
    print(" ___           _ _                         _                       ")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ")
    print(" | || '_ \ / _` | |/ _` | '_ \ / _` |  _  | |/ _ \| '_ \ / _ \/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\__ \\")
    print("|___|_| |_|\__,_|_|\__,_|_| |_|\__,_|  \___/ \___/|_| |_|\___||___/")
    print("                       and his Great Escape                        ")
    print()

    # rendering the dark room
    show_room(room)

    # main loop
    while game_state == states.PLAYING:
        # normalizing string
        line = input('> ').lower().strip()

        # empty input
        if line == '':
            continue

        # quit game
        elif line in ('koniec', 'quit', 'bye', 'q'):
            game_state = states.QUIT

        # about game
        elif line in ('o hre', 'about', 'info', '?'):
            print('(c)2021 created by mirek')
            print('Ďalšie veľké dobrodružstvo Indiana Jonesa. Tentokrát zápasí s jazykom Python v tmavej miestnosti.')

        # show commands
        elif line in ('prikazy', 'commands', 'help', 'pomoc'):
            print('Zoznam príkazov v hre:')
            print('* koniec - ukončí rozohratú hru')
            print('* o hre - zobrazí informácie o hre')
            print('* prikazy - zobrazí príkazy, ktoré sa dajú použiť v hre')
            print('* rozhliadni sa - vypíše opis miestnosti, v ktorej sa hráč práve nachádza')

        # render room
        elif line in ("rozhliadni sa", "look around", "kukaj het"):
            show_room(room)

        # unknown commands
        else:
            print('Taký príkaz nepoznám.')

    # game credits
    print('(c)2021 by mirek mocný programátor')
