from pydantic import BaseModel

from commands import *
from commands.command import Command
from items.item import Item
from rooms.room import Room
from rooms.world import load_world
from states import PLAYING


class GameContext(BaseModel):
    current_room: Room = None
    rooms: list[Room] = load_world()
    backpack: list[Item] = []
    commands: list[Command] = [
        About(),
        Commands(),
        Down(),
        Drop(),
        East(),
        Examine(),
        Help(),
        Inventory(),
        Load(),
        LookAround(),
        North(),
        Quit(),
        Save(),
        Score(),
        South(),
        Take(),
        Up(),
        Use(),
        West()
    ]
    game_state: str = PLAYING
    history: list[str] = []
    score = 0
