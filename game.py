#!/usr/bin/env python3
from world import world
from commands import *


def main():
    current_room = 'pred jaskynou'
    backpack = [
        {
            'name': 'bic',
            'description': 'Ta mocny bic na krotenie levov, ktory si si zohnal ako mlady chalanisko v tretej casti serie.',
            'features': ['movable', 'usable'],
        }
    ]

    commands = [
        About(),
        LookAround(),
        Inventory(),
        Commands(),
        Help(),
        North(),
        South(),
        East(),
        West(),
        Down(),
        # Up(),
        UseItem(),
        DropItem(),
        TakeItem(),
        ExamineItem
    ]

    print("Indiana Jones")
    show_room(world[current_room])

    answer = None

    while answer != 'koniec':
        answer = input('> ').strip().lower()

        for command in commands:
            if answer.startswith(command._name):
                command.exec(current_room, world, backpack)
                break
        else:
            print('Taký príkaz nepoznám.')

        # if answer == 'rozhliadni sa':
        #     cmd = LookAround()
        #     cmd.exec(world[current_room])
        #
        # elif answer == 'o hre':
        #     cmd = About()
        #     cmd.exec()
        #     # About().exec()
        #
        # elif answer == 'pomoc':
        #     help()
        #
        # elif answer == 'prikazy':
        #     commands()
        #
        # elif answer == 'koniec':
        #     quit()
        #
        # elif answer == 'vychod':
        #     current_room = east(world, current_room)
        #
        # elif answer == 'zapad':
        #     current_room = west(world, current_room)
        #
        # elif answer == 'sever':
        #     current_room = north(world, current_room)
        #
        # elif answer == 'juh':
        #     current_room = south(world, current_room)
        #
        # elif answer == 'dolu':
        #     current_room = down(world, current_room)
        #
        # elif answer == 'inventar':
        #     show_inventory(backpack)
        #
        # elif answer.startswith('poloz'):
        #     name = answer.lstrip('poloz').strip()
        #     drop_item(world, current_room, backpack, name)
        #
        # elif answer.startswith('vezmi'):
        #     name = answer.lstrip('vezmi').strip()
        #     take_item(world, current_room, backpack, name)
        #
        # elif answer.startswith('preskumaj'):
        #     name = answer.lstrip('preskumaj').strip()
        #     examine_item(world, current_room, backpack, name)
        #
        # elif answer.startswith('pouzi'):
        #     name = answer.lstrip('pouzi').strip()
        #     use_item(world, current_room, backpack, name)
        #
        # else:
        #     print('ta taky prikaz nepoznam')


if __name__ == '__main__':
    main()
