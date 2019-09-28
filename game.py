#!/usr/bin/env python3
# from game_context import GameContext
from backpack import Backpack
from helper import show_room
import game_context
from items import Whip
from world import world
from commands import *


def main():
    # inicializacia hry
    context = game_context.GameContext()
    context.current_room = 'pred jaskynou'
    context.backpack = Backpack(2)
    context.backpack.add_item(Whip())
    context.world = world

    commands = [
        About(),
        LookAround(),
        Inventory(),
        Quit(),
        North(),
        South(),
        East(),
        West(),
        Down(),
        # Up(),
        UseItem(),
        DropItem(),
        TakeItem(),
        ExamineItem(),
        Save()
    ]

    commands.append(Commands(commands))
    commands.append(Help(commands))

    print("Indiana Jones")
    show_room(world[context.current_room])

    while context.state == 'playing':
        answer = input('> ').strip().lower()

        for command in commands:
            if answer.startswith(command.name):
                params = answer.lstrip(command.name).strip()
                command.params = params
                command.exec(context)
                break
        else:
            print('Taký príkaz nepoznám.')


if __name__ == '__main__':
    main()
