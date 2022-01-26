#!/usr/bin/env python3

from commands import cmd_about
from items import bucket, canister, door, matches, newspaper
from items.features import MOVABLE
from helpers import banner, get_item_by_name, show_room
import states


def play_game():

    # game initialization
    room = {
        "description": "Nachádzaš sa v tmavej miestnosti, v ktorej rozhodne chýbajú okná. "
        "Je tu značne šero a vlhko. Chladné kamenné steny dávajú tušiť, že "
        "sa nachádzaš v podzemí.",
        "items": [
            canister,
            door,
            matches,
            bucket,
        ],
        "exits": [],
        "name": "dungeon",
    }
    backpack = [newspaper]
    game_state = states.PLAYING

    # intro banner
    banner()
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
            cmd_about()


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
                item = get_item_by_name(name, room["items"])

                if item is not None:
                    if MOVABLE in item["features"]:
                        room["items"].remove(item)
                        backpack.append(item)
                        print(f"Do batohu si vložil predmet {name}.")
                    else:
                        print("Tento predmet sa nedá zobrať.")
                else:
                    print("Taký predmet tu nikde nevidím.")

        # unknown command
        else:
            print("Taký príkaz nepoznám.")

    print("Created by (c)2022 mirek")


if __name__ == "__main__":
    play_game()
