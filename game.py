#!/usr/bin/env python3
import states
from commands import About, Inventory, LookAround, Quit, Drop, Examine, Commands, Take
from context import Context
from helpers import show_room
from items import newspaper, door, bucket, canister, matches


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
    """
    Parse the command from input

    @param line: input from the user
    @param commands: list of commands
    @return: tuple with cmd and it's param, or None otherwise
    """
    for command in commands:
        if line.startswith(command.name):
            param = line.split(command.name)[1].strip()
            return command, param

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
        Commands(),
        Drop(),
        Examine(),
        Inventory(),
        LookAround(),
        Quit(),
        Take()
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
        try:
            cmd, param = parse(line, commands)
            cmd.exec(context, param)
        except TypeError:
            print('Taký príkaz nepoznám.')

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

    # credits
    outro()


if __name__ == '__main__':
    main()
