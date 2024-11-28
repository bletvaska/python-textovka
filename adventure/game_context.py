from pydantic import BaseModel

from commands.about import About
from commands.command import Command
from commands.commands import Commands
from commands.down import Down
from commands.drop import Drop
from commands.examine import Examine
from commands.inventory import Inventory
from commands.look_around import LookAround
from commands.quit import Quit
from commands.take import Take
from items.item import Item
from rooms.room import Room
from rooms.world import get_world
from states import PLAYING


class GameContext(BaseModel):
    backpack: list[Item] = []
    commands: list[Command] = [
        About(),
        Commands(),
        Down(),
        Drop(),
        Examine(),
        Inventory(),
        LookAround(),
        Quit(),
        Take(),
    ]
    game_state: str = PLAYING
    current_room: Room = None
    world: list[Room] = get_world()
