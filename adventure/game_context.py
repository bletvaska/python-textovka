from pydantic import BaseModel

from items.item import Item
from rooms.room import Room
from states import PLAYING


class GameContext(BaseModel):
    current_room: Room = None
    rooms: list[Room] = []
    backpack: list[Item] = []
    commands: list = []
    game_state: str = PLAYING
    history: list[str] = []
