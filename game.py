#!/usr/bin/env python3
import states

from commands import cmd_about, cmd_commands, cmd_show_inventory, cmd_drop_item, cmd_take_item, cmd_quit, \
    cmd_examine_item, cmd_look_around
from helpers import show_room
from items import figa, coin, canister, matches, fire_extinguisher, newspaper, door


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
            cmd_look_around(context)

        # show inventory
        elif line in ("inventar", "i", "inventory", 'batoh'):
            cmd_show_inventory(context)

        # drop item
        elif line.startswith('poloz'):
            cmd_drop_item(line, context)

        # take item
        elif line.startswith('vezmi'):
            cmd_take_item(line, context)

        # examine item
        elif line.startswith('preskumaj'):
            cmd_examine_item(line, context)

        # unknown commands
        else:
            print('Taký príkaz nepoznám.')

    # game credits
    print('(c)2021 by mirek mocný programátor')
