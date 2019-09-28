#!/usr/bin/env python3
# from game_context import GameContext
from backpack import Backpack
from exceptions import UnknownCommandException
import game_context
from items import Whip
from parser import Parser
from world import world
from commands import *


def main():
    # inicializacia hry
    context = game_context.GameContext()
    context.init_game()
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

    parser = Parser(commands)

    print("Indiana Jones")
    context.get_current_room().show()
    # show_room(world[context.current_room])

    while context.state == 'playing':
        line = input('> ')

        try:
            command = parser.parse(line)
            command.exec(context)
        except UnknownCommandException:
            print('Taký príkaz nepoznám.')


if __name__ == '__main__':
    main()
