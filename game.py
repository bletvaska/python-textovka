#!/usr/bin/env python3

from commands import cmd_about, cmd_commands, cmd_drop, cmd_examine, cmd_inventory, cmd_take
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
            cmd_drop(room, backpack, line)

        # about game
        elif line in ("o hre", "about", "info"):
            cmd_about()

        # examine item
        elif line.startswith("preskumaj"):
            cmd_examine(room, backpack, line)

        # list of commands
        elif line in ("prikazy", "commands", "help", "?"):
            cmd_commands()

        # look around
        elif line in ("rozhliadni sa", "look around"):
            show_room(room)

        # inventory
        elif line in ("inventar", "i", "inventory"):
            cmd_inventory(backpack)

        # quit game
        elif line in ("koniec", "quit", "q", "bye"):
            line = input("Naozaj chceš skončiť? (a/n) ").lower().lstrip().rstrip()
            if line == "a":
                game_state = states.QUIT

        # take item
        elif line.startswith(("vezmi", "take")):
            cmd_take(room, backpack, line)

        # unknown command
        else:
            print("Taký príkaz nepoznám.")

    print("Created by (c)2022 mirek")


if __name__ == "__main__":
    play_game()
