from commands.command import Command
from room import Room


def intro():
    """
    Prints the intro banner of the game.

    Simple function which shows mocny banner on the screen.
    The banner is a representation of ascii art.
    """
    print(" ___           _ _                         _                         ____  ")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___  |___ \\ ")
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|   __) |")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\  / __/ ")
    print("|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/ |_____|")
    print('and his Great Python Adventure'.center(80))


def outro():
    """
    Prints the outro messages of the game.
    """
    print('(c)2022 by mirek')
    print('See you soon.')


def parse_line(line: str, commands: list[Command]) -> Command | None:
    for command in commands:
        if line.startswith(command.name):
            command.param = line.split(command.name, maxsplit=1)[1].lstrip()
            return command

    return None  # default


def get_room_by_name(name: str, rooms: list[Room]) -> Room | None:
    pass
