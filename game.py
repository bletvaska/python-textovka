#!/usr/bin/env python3

from turtle import back
from features import MOVABLE, USABLE
import states


def get_item_by_name(name: str, items: dict):
    for item in items:
        if name == item["name"]:
            return item

    # return None


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
            print(f"   {item['name']}")

    # return None


def play_game():

    # game initialization
    room = {
        "description": "Nachádzaš sa v tmavej miestnosti, v ktorej rozhodne chýbajú okná. "
        "Je tu značne šero a vlhko. Chladné kamenné steny dávajú tušiť, že "
        "sa nachádzaš v podzemí.",
        "items": [
            {
                "name": "kanister",
                "description": "Veľký 10 litrový kanister žltej farby. Značka: plný vysokooktánového výborne horľavého benzínu.",
                "features": [MOVABLE, USABLE],
            },
            {
                "name": "dvere",
                "description": "Veľké masívne dubové dvere. Zamknuté. Asi zvonka.",
                "features": [],
            },
            {
                "name": "zapalky",
                "description": "Bezpečnostné zápalky. Zrejme kúpené v Bille.",
                "features": [MOVABLE, USABLE],
            },
            {
                "name": "vedro",
                "description": "12 litrové vedro plné vody. V niektorých končinách nazývané aj kýbľom.",
                "features": [MOVABLE, USABLE],
            },
        ],
        "exits": [],
        "name": "dungeon",
    }
    backpack = [
        {
            "name": "noviny",
            "description": "Košické tajmsy. Dnešné, ešte teplé vydanie.",
            "features": [MOVABLE],
        }
    ]
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
        elif line.startswith(("poloz", "drop")):
            name = line.split(sep="poloz")[1].lstrip()

            # poloz
            # > Neviem, čo chceš položiť.
            if len(name) == 0:
                print("Neviem, aký predmet chceš položiť.")

            else:
                # poloz minca
                # > Predmet minca si položil v miestnosti.
                item = get_item_by_name(name, backpack)

                if item is None:
                    print("Taký predmet pri sebe nemáš.")
                else:
                    # poloz ho do miestnosti
                    room["items"].append(item)

                    # zmaz ho z batohu
                    backpack.remove(item)

                    # render
                    print(f"Do miestnosti si vyložil predmet {name}.")

        # about game
        elif line in ("o hre", "about", "info"):
            print(
                "Ďalšie dobrodružstvo Indiana Jonesa. Tentkrát sa snaží ujsť z uzavretej kobky pod zemou."
            )
            print("Túto hru spáchal v 2022 (c) mirek.")

        # examine item
        elif line.startswith("preskumaj"):
            name = line.split(sep="preskumaj")[1].lstrip()

            if len(name) == 0:
                print("Neviem, čo chceš preskúmať.")
            else:
                item = get_item_by_name(name, backpack + room["items"])

                if item is None:
                    print("Tento predmet tu nikde nevidím.")
                else:
                    print(item["description"])

        # list of commands
        elif line in ("prikazy", "commands", "help", "?"):
            print("Zoznam dostupných príkazov:")
            print("  * inventar - vypíše obsah batohu")
            print("  * koniec - ukončí rozohratú hru")
            print("  * o hre - zobrazí informácie o hre")
            print("  * poloz - vylozi predmet z batohu do aktuálnej miestnosti")
            print("  * preskumaj - zobrazí opis zvoleného predmetu")
            print("  * prikazy - zobrazí zoznam príkazov hry")
            print(
                "  * rozhliadni sa - Vypise popis miestnosti, kde sa prave nachadzas."
            )
            print("  * vezmi - vezme predmet a miestnosti a vloží si ho do batohu")

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
                    print(f" * {item['name']}")

        # quit game
        elif line in ("koniec", "quit", "q", "bye"):
            line = input("Naozaj chceš skončiť? (a/n) ").lower().lstrip().rstrip()
            if line == "a":
                game_state = states.QUIT

        # take item
        elif line.startswith(("vezmi", "take")):
            name = line.split(sep="vezmi")[1].lstrip()

            if len(name) == 0:
                print("Neviem, aký predmet chceš vziať.")

            else:
                for item in room["items"]:
                    if name == item["name"]:
                        if MOVABLE in item["features"]:
                            room["items"].remove(item)
                            backpack.append(item)
                            print(f"Do batohu si vložil predmet {name}.")

                        else:
                            print("Tento predmet sa nedá zobrať.")

                        break
                else:
                    print("Taký predmet tu nikde nevidím.")

        # unknown command
        else:
            print("Taký príkaz nepoznám.")

    print("Created by (c)2022 mirek")


if __name__ == "__main__":
    play_game()
