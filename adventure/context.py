from pydantic import BaseModel

import states
from items.item import Item
from rooms import Room


class Context(BaseModel):
    current_room: Room
    commands: list
    world: list[Room]
    game_state = states.PLAYING
    backpack: list[Item] = []
