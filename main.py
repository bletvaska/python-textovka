#!/usr/bin/env python

import states
from commands.about import About
from commands.drop import Drop
from commands.inventory import Inventory
from commands.lookaround import LookAround
from items.features import MOVABLE, USABLE
from helpers import get_item_by_name
from items.item import Item
from room import Room


def intro():
    """
    Shows the intro screen of the game.
    """
    print(" ___           _ _                         _")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___")
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\")
    print("|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/")
    print('                        and his Great Escape')
    print()


def outro():
    """
    Shows the outro screen of the game.
    """
    print('(c)2022 by mirek')
    print('See you soon.')


def main():
    # game init
    game_state = states.PLAYING
    backpack = []

    room = Room(name='dungeon',
                description='Nachádzaš sa vo veľmi tmavej miestnosti. Kamenné múry dávajú tušiť, že sa'
                            'nachádzaš v nejakej kamennej kobke. Žeby podzemie hradu v Grunwalde? '
                            'Okná tu nie sú žiadne, čo by ťa uistilo o správnosti tohto predpokladu.',
                items=[
                    Item(name='zapalky',
                         description='Štandardné zápalky. Tri.',
                         features=[MOVABLE, USABLE]),
                    Item(name='vedro',
                         description='Vedro plné vody. Ťažko povedať, či aj pitnej.',
                         features=[MOVABLE, USABLE]),
                    Item(name='kanister',
                         description='Veľký 25l kanister. Po odšróbovaní vrchnáka si zistil, že je to benzín. Kvalitka. 98 oktánov.',
                         features=[USABLE, MOVABLE]),
                    Item(name='dvere',
                         description='Veľké dubové dvere. Zamknuté.',
                         features=[])
                ],
                exits=[
                    'sever',
                    'juh'
                ]
                )

    room.show()

    # game loop
    while game_state == states.PLAYING:
        line = input('> ').lstrip().rstrip().lower()

        if line == '':
            continue

        # rozhliadni sa, look around
        elif line in ('rozhliadni sa', 'look around'):
            cmd = LookAround()
            cmd.exec(room)

        # about, info, ?
        elif line in ('o hre', 'about', 'info', '?'):
            cmd = About()
            cmd.exec()

        # drop item
        elif line.startswith('poloz'):
            cmd = Drop()
            cmd.exec(line, backpack, room)

        # take item
        elif line.startswith('vezmi'):
            # extraction of item to vezmi
            name = line.split('vezmi')[1].lstrip()

            # if no item was entered...
            if name == '':
                print('Neviem, co chceš zobrať.')

            else:
                # is the item in room?
                item = get_item_by_name(name, room.items)

                if item is None:
                    print('Taký predmet tu nevidím.')

                else:
                    # is it movable?
                    if MOVABLE not in item.features:
                        print('Tento predmet sa nedá zobrať.')

                    else:
                        # vezmi item
                        # vezmi item z miestnosti
                        room.items.remove(item)

                        # add item to backpack items
                        backpack.append(item)

                        # render
                        print(f'Predmet {item.name} si si vložil do batohu.')

        # commands, help
        elif line in ('prikazy', 'help', 'commands'):
            print('Zoznam príkazov v hre:')
            print('* inventar - zobrazí obsah hráčovho batohu')
            print('* koniec - skončenie programu')
            print('* o hre - vypíše info o hre')
            print('* poloz - položí predmet z batohu do aktuálnej miestnosti')
            print('* prikazy - vypíše zoznam príkazov')
            print('* rozhliadni sa - vypíše opis aktuálnej miestnosti')
            print('* vezmi - vezme predmet z miestnosti a vloží si ho do batohu')

        # quit, exit, q, bye
        elif line in ('koniec', 'quit', 'exit', 'q', 'bye'):
            print('Naozaj chceš skončiť? (a/n)')
            line = input('>> ').lower().strip()
            if line in ('a', 'ano', 'y', 'yes'):
                print('Dakujem, ze si si zahral tuto fantasticku hru. Príď aj nabudúce.')
                game_state = states.QUIT
            else:
                continue

        # inventory
        elif line in ('inventar', 'i', 'inventory'):
            cmd = Inventory()
            cmd.exec(backpack)

        else:
            print('Taký príkaz nepoznám.')


if __name__ == '__main__':
    intro()
    main()
    outro()
