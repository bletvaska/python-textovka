from dataclasses import dataclass

from commands.command import Command
from items.item import Item
from rooms.room import Room


@dataclass
class GameContext:
    game_state: str
    commands: list[Command]
    backpack: list[Item]
    current_room: Room
