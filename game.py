#!/usr/bin/env python3
import states
from typing import Dict

from commands import cmd_about, cmd_commands, cmd_show_inventory, cmd_drop_item, cmd_take_item, cmd_quit
from items import figa, coin, canister, matches, fire_extinguisher, newspaper, door


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
        # print(f"Vidíš: {', '.join(room['items'])}")
        for item in room['items']:
            print(f"   * {item['name']}")

    # return None


if __name__ == '__main__':
    # init game
    context = {
        'state': states.PLAYING,
        'backpack': {
            'items': [],
            'max': 2,
        },
        'world': {},
        'room': {}
    }

    context['backpack']['items'].append(figa)
    context['backpack']['items'].append(coin)

    context['room'] = {
        'name': 'dungeon',
        'description': 'Nachádzaš sa v tmavej zatuchnutej miestnosti. Na kamenných stenách sa nenachádza žiadne okno, '
                       'čo dáva tušiť, že si niekoľko metrov pod zemou. Žeby košický hrad? Aj to je možné, ti '
                       'prebleslo hlavou.',
        'items': [
            canister,
            matches,
            fire_extinguisher,
            newspaper,
            door
        ],
        'exits': []
    }

    # banner
    print(" ___           _ _                         _                       ")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ")
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\")
    print("|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/")
    print("                       and his Great Escape                        ")
    print()

    # rendering the dark room
    show_room(context['room'])

    # main loop
    while context['state'] == states.PLAYING:
        # normalizing string
        line = input('> ').lower().strip()

        # empty input
        if line == '':
            continue

        # quit game
        elif line in ('koniec', 'quit', 'bye', 'q', 'exit'):
            cmd_quit(context)

        # about game
        elif line in ('o hre', 'about', 'info', '?'):
            cmd_about(context)

        # show commands
        elif line in ('prikazy', 'commands', 'help', 'pomoc'):
            cmd_commands(context)

        # render room
        elif line in ("rozhliadni sa", "look around", "kukaj het"):
            show_room(context['room'])

        # show inventory
        elif line in ("inventar", "i", "inventory", 'batoh'):
            cmd_show_inventory(context)

        # drop item
        elif line.startswith('poloz'):
            cmd_drop_item(line, context)

        # take item
        elif line.startswith('vezmi'):
            cmd_take_item(line, context)

        # unknown commands
        else:
            print('Taký príkaz nepoznám.')

    # game credits
    print('(c)2021 by mirek mocný programátor')
