from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_context import GameContext
from commands.command import Command
from items.item import Item
from rooms.room import Room


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
    print()


def outro():
    """
    Prints the outro messages of the game.
    """
    print('Tento remake vytvoril mirek sko súčasť svojich školení v rokoch 2022-2023.')
    print('Originálnu hru vytvoril v roku 1986 František Fuka aka Fuxoft.')
    print('See you soon.')


def parse_line(line: str, context: 'GameContext') -> Command | None:
    """
    Returns command object based on the input entered by user.
    """
    for command in context.commands:
        if line.startswith(command.name):
            command.param = line.split(command.name, maxsplit=1)[1].lstrip()
            return command

    return None  # default


def get_room_by_name(name: str, context: 'GameContext') -> Room | None:
    """
    Returns room by its name.
    """
    for room in context.rooms:
        if room.name == name:
            return room

    return None  # default


def get_item_by_name(name: str, items: list[Item]) -> Item | None:
    for item in items:
        if item.name == name:
            return item

    return None  # default
