#!/usr/bin/env python3

import states

room = {
    "description": "Nachádzaš sa v tmavej miestnosti, v ktorej rozhodne chýbajú okná. "
    "Je tu značne šero a vlhko. Chladné kamenné steny dávajú tušiť, že "
    "sa nachádzaš v podzemí.",
    "items": ['kanister', 'zapalky', 'vedro'],
    "exits": [],
    "name": "dungeon",
}


def show_room(room: dict):
    """
    Shows the room description

    This function shows the room description, which contains the room name,
    room description, items in room and list of exists.
    :param room: the room to show description about
    """
    print(f"Nachádzaš sa v miestnosti {room['name']}")
    print(room["description"])

    # show exits
    if len(room["exits"]) == 0:
        print("Z tejto miestnosti nevedú žiadne východy.")

    # show items
    if len(room['items']) == 0:
        print("Nenachadzaju sa tu ziadne predmety")
    else:
        print("Vidíš: ")
        for item in room['items']:
            print(f'   {item}')

    # return None


def play_game():
    print(" ___           _ _                         _                       ")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ")
    print(" | || '_ \ / _` | |/ _` | '_ \ / _` |  _  | |/ _ \| '_ \ / _ \/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\__ \\")
    print("|___|_| |_|\__,_|_|\__,_|_| |_|\__,_|  \___/ \___/|_| |_|\___||___/")
    print("             Indiana Jones and his Great Escape")
    print()

    # print(room['description'])
    show_room(room)

    game_state = states.PLAYING

    while game_state == states.PLAYING:

        # normalizing input string
        line = input("> ").lower().lstrip().rstrip()

        # empty input?
        if line == "":
            continue

        # about game
        elif line in ("o hre", "about", "info"):
            print(
                "Ďalšie dobrodružstvo Indiana Jonesa. Tentkrát sa snaží ujsť z uzavretej kobky pod zemou."
            )
            print("Túto hru spáchal v 2022 (c) mirek.")

        # list of commands
        elif line in ("prikazy", "commands", "help", "?"):
            print("Zoznam dostupných príkazov:")
            print("  * koniec - ukončí rozohratú hru")
            print("  * o hre - zobrazí informácie o hre")
            print("  * prikazy - zobrazí zoznam príkazov hry")
            print(
                "  * rozhliadni sa - Vypise popis miestnosti, kde sa prave nachadzas."
            )

        # look around
        elif line in ("rozhliadni sa", "look around"):
            # print(room['description'])
            show_room(room)

        # quit game
        elif line in ("koniec", "quit", "q", "bye"):
            line = input("Naozaj chceš skončiť? (a/n) ").lower().lstrip().rstrip()
            if line == "a":
                game_state = states.QUIT

        # unknown command
        else:
            print("Taký príkaz nepoznám.")

    print("Created by (c)2022 mirek")


if __name__ == "__main__":
    play_game()
