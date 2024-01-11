from pydantic import BaseModel

from commands.command import Command
from items.item import Item
from rooms.room import Room
import states


class GameContext(BaseModel):
    game_state: str = states.PLAYING
    current_room: Room
    backpack: list[Item] = []
    commands: list[Command]
