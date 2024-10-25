from pydantic import BaseModel

from commands.command import Command
from rooms.room import Room
from states import PLAYING


class GameContext(BaseModel):
    backpack: list = []
    commands: list[Command] = []
    game_state: str = PLAYING
    current_room: Room = None
