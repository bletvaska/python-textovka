from pyfiglet import Figlet

from items.item import Item
from rooms import Room


def intro():
    """
    Shows the intro screen of the game.
    """
    figlet = Figlet()
    banner = figlet.renderText('Indiana Jones')
    print(banner)
    print('                        and his Great Python Adventure')
    print()

    # return None


def outro():
    """
    Shows the outro screen of the game.
    """
    print('(c)2023 by mirek')
    print('Thanks for playing')

    # return None


def get_item_by_name(name: str, items: list[Item]) -> Item | None:
    for item in items:
        if item.name == name:
            return item

    # return None


def get_room_by_name(name: str, rooms: list[Room]) -> Room | None:
    for room in rooms:
        if room.name == name:
            return room

    # return None
