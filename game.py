#!/usr/bin/env python3
import states
from commands import About, Inventory, LookAround, Quit
from context import Context
from helper import show_room, get_item_by_name
from items import newspaper, door, bucket, canister, matches
from items.features import MOVABLE


def intro():
    """
    Shows intro.

    This function shows intro banner for the game.
    """
    print(" ___           _ _                         _")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___")
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\")
    print("|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/")

    print("Indiana Jones and his Great Escape".center(70))


def outro():
    """
    Shows outro (credits).

    This functions shows credits at the end of the game. This is the last test, the player will see.
    """
    print('*-' * 35)
    print('Created by (c) mirek - A very talented young python programmer.')
    print('Please support his next magic project by sending some funds')
    print('(at least 100 Euros). He will create something.')


def parse(line: str, commands):
    for command in commands:
        if command.name == line:
            return command

    # return None


def main():
    # game init
    context = Context(
        backpack=[
            matches,
        ],

        room={
            "description": 'Nachádzaš sa v miestnosti plnej ružových slonov. Aby si si neublížil, tak stena je pokrytá '
                           'vankúšikmi. Tiež ružovými. Žiadne okno ti neposkytne rozkošný pohľad na vonkajšiu faunu a '
                           'flóru.',
            "items": [
                door,
                bucket,
                newspaper,
                canister
            ],
            "exits": {
                'north': 'zahradka',
                'south': None,
                'east': 'jaskyna',
                'west': None
            },
            "name": 'miestnost',
        },
    )

    commands = [
        About(),
        Inventory(),
        LookAround(),
        Quit()
    ]

    # intro
    intro()

    show_room(context.room)

    # game loop
    while context.game_state == states.PLAYING:
        line = input('> ').lstrip().rstrip().lower()

        if line == '':
            continue  # pass

        # parse line
        cmd = parse(line, commands)
        if cmd is None:
            print('Taký príkaz nepoznám.')
        else:
            cmd.exec(context)

        # elif line in ('o hre', 'about', 'info'):
        #     print('Ďalšie napínavé dobrodružstvo Indiana Jonesa. Tentokrát sa Indy ...')
        #     print('Túto nadupanú hru spáchal (c) mirek')
        #
        # elif line in ('prikazy', 'commands', 'help', '?',):
        #     print('Dostupné príkazy v hre:')
        #     print('* o hre - zobrazí informácie o hre')
        #     print('* inventar - zobrazí obsah batohu')
        #     print('* koniec - ukončí hru')
        #     print('* poloz - vylozi predmet z batohu do miestnosti')
        #     print('* preskumaj - zobrazí opis zvoleného predmetu')
        #     print('* prikazy - zobrazí zoznam aktuálne dostupných príkazov')
        #     print('* rozhliadni sa - zobrazí opis miestnosti')
        #     print('* vezmi - vloží predmet do batohu')
        #
        # elif line in ('rozhliadni sa', 'look around'):
        #     show_room(room)
        #
        # elif line in ('koniec', 'quit', 'q', 'bye'):
        #     x = input('Naozaj chceš skončiť? (a/n) ').strip().lower()
        #     if x in ('a', 'ano', 'y', 'yes'):
        #         game_state = states.QUIT
        #     else:
        #         print('Tak hráme ďalej...')
        #
        # elif line in ('inventar', 'inventory', 'i'):
        #     if len(backpack) == 0:
        #         print('Batoh je prázdny.')
        #     else:
        #         print('V batohu máš:')
        #         for item in backpack:
        #             print(f' * {item.name}')
        #
        # elif line.startswith('poloz'):
        #     name = line.split('poloz')[1].strip()
        #
        #     # bol zadany nazov predmetu?
        #     if name == '':
        #         print('Neviem, čo chceš položiť.')
        #
        #     # je v batohu?
        #     else:
        #         item = get_item_by_name(name, backpack)
        #
        #         if item is None:
        #             print('Taký predmet pri sebe nemáš.')
        #         else:
        #             # vymazem z batohu
        #             backpack.remove(item)
        #
        #             # vlozim do miestnosti
        #             room['items'].append(item)
        #
        #             # render
        #             print(f'Do miestnosti si položil predmet {name}.')
        #
        # elif line.startswith('vezmi'):
        #     name = line.split('vezmi')[1].strip()
        #
        #     # bol zadany nazov predmetu?
        #     if name == '':
        #         print('Neviem, čo chceš vziať.')
        #
        #     # je v miestnosti?
        #     else:
        #         item = get_item_by_name(name, room['items'])
        #         if item is None:
        #             print('Taký predmet tu nikde nevidím.')
        #         else:
        #             # je prenositelny?
        #             if MOVABLE in item.features:
        #                 # vymazem z miestnosti
        #                 room['items'].remove(item)
        #
        #                 # vlozim do batohu
        #                 backpack.append(item)
        #
        #                 # render
        #                 print(f'Do batohu si si vložil predmet {name}.')
        #             else:
        #                 print('Tento predmet sa nedá zobrať.')
        #
        # elif line.startswith('preskumaj'):
        #     name = line.split('preskumaj')[1].strip()
        #
        #     # bol zadany nazov predmetu?
        #     if len(name) == 0:
        #         print('Neviem čo chceš preskúmať.')
        #
        #     else:
        #         item = get_item_by_name(name, room['items'] + backpack)
        #
        #         if item is None:
        #             print('Taký predmet tu nikde nevidím.')
        #         else:
        #             print(item.description)
        #
        # else:
        #     print('Taký príkaz nepoznám.')

    # credits
    outro()


if __name__ == '__main__':
    main()
