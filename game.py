#!/usr/bin/env python3
import states
from commands import About, Inventory, LookAround, Quit, Drop, Examine, Commands, Take, Use, West, South, North, East
from context import Context
from helpers import show_room
from items import matches
from world import world


def intro():
    """
    Shows intro.

    This function shows intro banner for the game.
    """
    print(" ___           _ _                         _")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___")
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\")
    print("|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/")

    print("Indiana Jones and his Great Escape".center(70))


def outro():
    """
    Shows outro (credits).

    This functions shows credits at the end of the game. This is the last test, the player will see.
    """
    print('*-' * 35)
    print('Created by (c) mirek - A very talented young python programmer.')
    print('Please support his next magic project by sending some funds')
    print('(at least 100 Euros). He will create something.')


def parse(line: str, commands):
    """
    Parse the command from input

    @param line: input from the user
    @param commands: list of commands
    @return: tuple with cmd and it's param, or None otherwise
    """
    for command in commands:
        if line.startswith(command.name):
            param = line.split(command.name)[1].strip()
            return command, param

    # return None


def main():
    # game init
    context = Context(
        world=world,

        backpack=[
            matches,
        ],

        room=world['kobka'],

        commands=[
            About(),
            Commands(),
            Drop(),
            East(),
            Examine(),
            Inventory(),
            LookAround(),
            North(),
            Quit(),
            South(),
            Take(),
            Use(),
            West(),
        ]
    )

    # intro
    intro()
    show_room(context.room)

    # game loop
    while context.game_state == states.PLAYING:
        line = input('> ').lstrip().rstrip().lower()

        if line == '':
            continue  # pass

        # parse line
        try:
            cmd, param = parse(line, context.commands)
            cmd.exec(context, param)
        except TypeError:
            print('Taký príkaz nepoznám.')

    # credits
    outro()


if __name__ == '__main__':
    main()
