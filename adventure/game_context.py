from pydantic import BaseModel

from commands.command import Command
from items.item import Item
from rooms.room import Room
from states import PLAYING


class GameContext(BaseModel):
    current_room: Room = None
    rooms: list[Room] = []
    backpack: list[Item] = []
    commands: list[Command] = []
    game_state: str = PLAYING
    history: list[str] = []
    score = 0
