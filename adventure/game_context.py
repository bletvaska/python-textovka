from pydantic import BaseModel

from commands.about import About
from commands.command import Command
from commands.commands import Commands
from commands.drop import Drop
from commands.examine import Examine
from commands.inventory import Inventory
from commands.look_around import LookAround
from commands.quit import Quit
from commands.take import Take
from rooms.room import Room
from states import PLAYING


class GameContext(BaseModel):
    backpack: list = []
    commands: list[Command] = [
        About(),
        Commands(),
        Drop(),
        Examine(),
        Inventory(),
        LookAround(),
        Quit(),
        Take()
    ]
    game_state: str = PLAYING
    current_room: Room = None
    history: list[str] = []
