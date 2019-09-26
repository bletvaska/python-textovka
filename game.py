#!/usr/bin/env python3
from game_context import GameContext
from world import world
from commands import *


def main():
    # inicializacia hry
    context = GameContext()
    context.current_room = 'pred jaskynou'
    context.backpack = [
        {
            'name': 'bic',
            'description': 'Ta mocny bic na krotenie levov, ktory si si zohnal ako mlady chalanisko v tretej casti serie.',
            'features': ['movable', 'usable'],
        }
    ]
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
