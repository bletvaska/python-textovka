from commands.command import Command
from game_context import GameContext
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
    print('(c)2022 by mirek')
    print('See you soon.')


def parse_line(line: str, commands: list[Command]) -> Command | None:
    """
    Returns command object based on the input entered by user.
    """
    for command in commands:
        if line.startswith(command.name):
            command.param = line.split(command.name, maxsplit=1)[1].lstrip()
            return command

    return None  # default


def get_room_by_name(name: str, rooms: list[Room]) -> Room | None:
    """
    Returns room by its name.
    """
    for room in rooms:
        if room.name == name:
            return room

    return None  # default


def get_current_room(context: GameContext) -> Room:
    """
    Returns current room.
    """
    return get_room_by_name(context.current_room, context.rooms)


def get_item_by_name(name: str, items: list[Item]) -> Item | None:
    for item in items:
        if item.name == name:
            return item

    return None  # default
