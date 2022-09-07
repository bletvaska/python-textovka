from commands.command import Command
from items.item import Item


class Context:
    game_state: str
    commands: list[Command]
    backpack: list[Item]