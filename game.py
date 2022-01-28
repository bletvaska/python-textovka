#!/usr/bin/env python3

from commands import (
    About,
    East,
    LookAround,
    Quit,
    Inventory,
    TakeItem,
    ExamineItem,
    DropItem,
    ListOfCommands,
    UseItem,
    West,
    North,
    South,
)
from items import bucket, canister, door, matches, newspaper
from helpers import banner, get_room_by_name, show_room
from models import Context
import states
import json
# from world import world


def play_game():
    # load world
    file = open('assets/world.json', 'r')
    world = json.load(file)
    dungeon = get_room_by_name('dungeon', world)
    dungeon['items'].append(canister)
    # dungeon['items'].append(door)
    dungeon['items'].append(matches)
    dungeon['items'].append(bucket)
    file.close()

    # context
    context = Context(
        room=get_room_by_name("dungeon", world),
        backpack=[newspaper],
        world=world,
        commands=[
            About(),
            DropItem(),
            East(),
            ExamineItem(),
            Inventory(),
            ListOfCommands(),
            LookAround(),
            North(),
            Quit(),
            South(),
            TakeItem(),
            UseItem(),
            West(),
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
            continue

        # state evaluation
        if context.room["name"] == "heaven":
            context.state = states.WINNER
            print(
                "Ta aj svarny archeolog Indiana Jones sa nakoniec dostal do neba. Gratulujeme."
            )

        elif context.room["name"] == "hell":
            context.state = states.DEAD
            print(
                "Ta ani taky svarny archeolog ako je Indiana Jones sa nedokaze dostat z pruseru, ktorym je peklo. Je to pre neho Game Over."
            )

    print("Created by (c)2022 mirek")


if __name__ == "__main__":
    # file = open('assets/world.json', 'w')
    # json.dump(world, file, ensure_ascii=False, indent=4)
    # file.close()
    play_game()
