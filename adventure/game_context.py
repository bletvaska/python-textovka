from pydantic import BaseModel

from commands.about import About
from commands.command import Command
from commands.commands import Commands
from commands.examine import Examine
from commands.inventory import Inventory
from commands.look_around import LookAround
from commands.quit import Quit
from rooms.room import Room
from states import PLAYING


class GameContext(BaseModel):
    backpack: list = []
    commands: list[Command] = [
        About(),
        Commands(),
        Examine(),
        Inventory(),
        LookAround(),
        Quit()
    ]
    game_state: str = PLAYING
    current_room: Room = None
