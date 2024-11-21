from pydantic import BaseModel

from commands.about import About
from commands.command import Command
from commands.commands import Commands
from commands.inventory import Inventory
from commands.quit import Quit
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
