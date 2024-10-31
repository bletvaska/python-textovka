from pydantic import BaseModel

from commands.down import Down
from commands.east import East
from commands.north import North
from commands.save import Save
from commands.south import South
from commands.up import Up
from commands.use import Use
from commands.west import West
from rooms.room import Room
from commands.command import Command
from commands.about import About
from commands.commands import Commands
from commands.drop import Drop
from commands.examine import Examine
from commands.inventory import Inventory
from commands.look_around import LookAround
from commands.quit import Quit
from commands.take import Take
from rooms.world import get_world
from states import PLAYING


class GameContext(BaseModel):
    backpack: list = []
    commands: list[Command] = [
        About(),
        Commands(),
        Down(),
        Drop(),
        East(),
        Examine(),
        Inventory(),
        LookAround(),
        North(),
        Quit(),
        Save(),
        South(),
        Take(),
        Up(),
        Use(),
        West(),
    ]
    game_state: str = PLAYING
    current_room: Room = None
    history: list[str] = []
    world: list[Room] = get_world()
