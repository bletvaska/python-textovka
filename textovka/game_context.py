from pydantic import BaseModel

from rooms.room import Room
from states import STATE_PLAYING


class GameContext(BaseModel):
    current_room: Room
    backpack: list = []
    game_state: str = STATE_PLAYING
    commands: list
    world: list[Room]

