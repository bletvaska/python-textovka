from pydantic import BaseModel

from adventure.commands.command import Command
from adventure.items.item import Item
from adventure.rooms.room import Room
from adventure.rooms.world import load_world
from adventure.states import PLAYING


class GameContext(BaseModel):
    current_room: Room = None
    rooms: list[Room] = load_world()
    backpack: list[Item] = []
    commands: list[Command] = []
    game_state: str = PLAYING
    history: list[str] = []
    score: int = 0
