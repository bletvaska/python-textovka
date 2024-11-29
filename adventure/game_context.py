from pydantic import BaseModel

from commands.about import About
from commands.command import Command
from commands.commands import Commands
from commands.down import Down
from commands.drop import Drop
from commands.east import East
from commands.examine import Examine
from commands.inventory import Inventory
from commands.load import Load
from commands.look_around import LookAround
from commands.north import North
from commands.quit import Quit
from commands.restart import Restart
from commands.save import Save
from commands.south import South
from commands.take import Take
from commands.up import Up
from commands.west import West
from commands.use import Use
from helpers import get_room_by_name
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
        East(),
        Examine(),
        Inventory(),
        Load(),
        LookAround(),
        North(),
        Quit(),
        Restart(),
        Save(),
        South(),
        Take(),
        Up(),
        Use(),
        West(),
    ]
    game_state: str = PLAYING
    current_room: Room = None
    world: list[Room] = get_world()
    history: list[str] = []

    def reset(self):
        self.game_state = PLAYING
        self.world = get_world()
        self.current_room = get_room_by_name('lietadlo', self.world)
        self.backpack = []
        self.history = []
