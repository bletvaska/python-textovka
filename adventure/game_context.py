from pydantic import BaseModel

from commands.about import About
from commands.command import Command
from commands.commands import Commands
from commands.inventory import Inventory
from commands.quit import Quit
from rooms.room import Room
from states import PLAYING


class GameContext(BaseModel):
    backpack: list = []
    commands: list[Command] = [
        About(),
        Commands(),
        Inventory(),
        Quit(),
    ]
    game_state: str = PLAYING
    current_room: Room = None
