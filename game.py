#!/usr/bin/env python3

from turtle import back
import states


def show_room(room: dict):
    """
    Shows the room description

    This function shows the room description, which contains the room name,
    room description, items in room and list of exists.
    :param room: the room to show description about
    """

    # type check for room
    if type(room) is not dict:
        raise TypeError(
            f'Inapropriate type for room. Expected dict, but "{type(room)}" was given.'
        )

    print(f"Nachádzaš sa v miestnosti {room['name']}")
    print(room["description"])

    # show exits
    if len(room["exits"]) == 0:
        print("Z tejto miestnosti nevedú žiadne východy.")

    # show items
    if len(room["items"]) == 0:
        print("Nenachadzaju sa tu ziadne predmety")
    else:
        print("Vidíš: ")
        for item in room["items"]:
            print(f"   {item}")

    # return None


def play_game():

    # game initialization
    room = {
        "description": "Nachádzaš sa v tmavej miestnosti, v ktorej rozhodne chýbajú okná. "
        "Je tu značne šero a vlhko. Chladné kamenné steny dávajú tušiť, že "
        "sa nachádzaš v podzemí.",
        "items": ["kanister", "zapalky", "vedro"],
        "exits": [],
        "name": "dungeon",
    }
    backpack = ["minca", "noviny", "figa borova"]
    game_state = states.PLAYING

    # intro banner
    print(" ___           _ _                         _                       ")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ")
    print(" | || '_ \ / _` | |/ _` | '_ \ / _` |  _  | |/ _ \| '_ \ / _ \/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\__ \\")
    print("|___|_| |_|\__,_|_|\__,_|_| |_|\__,_|  \___/ \___/|_| |_|\___||___/")
    print("             Indiana Jones and his Great Escape")
    print()

    show_room(room)

    while game_state == states.PLAYING:

        # normalizing input string
        line = input("> ").lower().lstrip().rstrip()

        # parser
        # empty input?
        if line == "":
            continue

        # drop item
        elif line.startswith(('poloz', 'drop')):
            name = line.split(sep='poloz')[1].lstrip()

            # poloz
            # > Neviem, čo chceš položiť.
            if len(name) == 0:
                print('Neviem, aký predmet chceš položiť.')

            else:
                # poloz minca
                # > Predmet minca si položil v miestnosti.
                if name in backpack:
                    # zmaz ho z batohu
                    backpack.remove(name)

                    # poloz ho do miestnosti
                    room['items'].append(name)

                    # render
                    print(f'Do miestnosti si vyložil predmet {name}.')

                else:
                    # poloz autobus
                    # > Taký predmet pri sebe nemáš.
                    print('Taký predmet pri sebe nemáš.')


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
            show_room(room)

        # inventory
        elif line in ("inventar", "i", "inventory"):
            if backpack == []:
                print("Batoh je prázdny.")
            else:
                print("V batohu máš:")
                for item in backpack:
                    print(f" * {item}")

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
