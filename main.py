#!/usr/bin/env python3
import states
from commands import About, Commands, Quit, Command
from helpers import intro, outro


def parse_line(line: str, commands: list[Command]):
    for command in commands:
        if line == command.name:
            return command

    return None


# game initialization
game_state = states.PLAYING
commands = [
    About(),
    Commands(),
    Quit()
]

# game loop
intro()
while game_state == states.PLAYING:
    line = input('> ').lower().lstrip().rstrip()  # echo line | lower | lstrip | rstrip

    # is line empty?
    if line == '':  # if len(line) == 0:
        continue  # {}

    # parse and execute command
    command = parse_line(line, commands)
    if command is None:
        print('Taký príkaz nepoznám.')
    else:
        command.exec()

    # try:
    #     command = parse_line(line, commands)
    #     command.exec()
    # except AttributeError:
    #     print('Taký príkaz nepoznám.')

outro()
