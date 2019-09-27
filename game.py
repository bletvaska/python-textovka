#!/usr/bin/env python3
from backpack import Backpack
from game_context import GameContext
from items import Whip, Bag
from world import world
from commands import *


def main():
    # inicializacia hry
    context = GameContext()
    context.current_room = 'pred jaskynou'
    context.world = world

    context.backpack = Backpack(2)
    context.backpack.add(Whip())
    context.backpack.add(Bag())

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
        ExamineItem()
    ]

    commands.append(Commands(commands))
    commands.append(Help(commands))

    print("Indiana Jones")
    show_room(world[context.current_room])

    while context.state == 'playing':
        answer = input('> ').strip().lower()

        for command in commands:
            if answer.startswith(command._name):
                params = answer.lstrip(command._name).strip()
                command.set_params(params)
                command.exec(context)
                break
        else:
            print('Taký príkaz nepoznám.')


if __name__ == '__main__':
    main()
