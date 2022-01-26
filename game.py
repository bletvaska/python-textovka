#!/usr/bin/env python3

from ast import AsyncFunctionDef
from dataclasses import dataclass
from typing import List
from commands import (
    cmd_about,
    cmd_commands,
    cmd_drop,
    cmd_examine,
    cmd_inventory,
    cmd_quit,
    cmd_take,
)
from items import bucket, canister, door, matches, newspaper
from items.features import MOVABLE
from helpers import banner, get_item_by_name, show_room
from models import Context
import states


def play_game():
    # context
    context = Context(
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
        },
        backpack = [ newspaper ],
        world = {}
    )

    # intro banner
    banner()
    show_room(context.room)

    while context.state == states.PLAYING:

        # normalizing input string
        line = input("> ").lower().lstrip().rstrip()

        # parser
        # cmd = parse(line)
        # if cmd is None:
        #     print()
        # else:
        #     cmd.exec()
        # empty input?
        if line == "":
            continue

        # drop item
        elif line.startswith(("poloz", "drop")):
            cmd_drop(context, line)

        # about game
        elif line in ("o hre", "about", "info"):
            cmd_about(context, line)

        # examine item
        elif line.startswith("preskumaj"):
            cmd_examine(context, line)

        # list of commands
        elif line in ("prikazy", "commands", "help", "?"):
            cmd_commands(context, line)

        # look around
        elif line in ("rozhliadni sa", "look around"):
            show_room(context.room)

        # inventory
        elif line in ("inventar", "i", "inventory"):
            cmd_inventory(context, line)

        # quit game
        elif line in ("koniec", "quit", "q", "bye"):
            cmd_quit(context, line)

        # take item
        elif line.startswith(("vezmi", "take")):
            cmd_take(context, line)

        # unknown command
        else:
            print("Taký príkaz nepoznám.")

    print("Created by (c)2022 mirek")


if __name__ == "__main__":
    play_game()
