#!/usr/bin/env python3

from commands import (
    About,
    LookAround,
    Quit,
    Inventory,
    TakeItem,
    ExamineItem,
    DropItem,
    ListOfCommands,
    UseItem
)
from items import bucket, canister, door, matches, newspaper
from helpers import banner, show_room
from models import Context
import states


def play_game():
    # context
    context = Context(
        room={
            "description": "Nachádzaš sa v tmavej miestnosti, v ktorej rozhodne chýbajú okná. "
            "Je tu značne šero a vlhko. Chladné kamenné steny dávajú tušiť, že "
            "sa nachádzaš v podzemí.",
            "items": [
                canister,
                door,
                matches,
                bucket,
            ],
            "exits": {
                'north': None,
                'south': None,
                'east': None,
                'west': None
            },
            "name": "dungeon",
        },
        backpack=[newspaper],
        world={},
        commands=[
            About(),
            DropItem(),
            ExamineItem(),
            Inventory(),
            ListOfCommands(),
            LookAround(),
            Quit(),
            TakeItem(),
            UseItem()
        ],
    )

    # intro banner
    banner()
    show_room(context.room)

    while context.state == states.PLAYING:

        # normalizing input string
        line = input("> ").lower().lstrip().rstrip()

        # empty input?
        if line == "":
            continue

        # parser
        for command in context.commands:
            if line.startswith(command.name):
                param = line.split(sep=command.name)[1].lstrip()
                command.exec(context, param)
                break
        else:
            print("Taký príkaz nepoznám.")

    print("Created by (c)2022 mirek")


if __name__ == "__main__":
    play_game()
