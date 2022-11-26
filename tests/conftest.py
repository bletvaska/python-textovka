import pytest

from commands.about import About
from commands.commands import Commands
from commands.down import Down
from commands.drop import Drop
from commands.east import East
from commands.examine import Examine
from commands.help import Help
from commands.inventory import Inventory
from commands.look_around import LookAround
from commands.north import North
from commands.quit import Quit
from commands.south import South
from commands.take import Take
from commands.up import Up
from commands.use import Use
from commands.west import West

from game_context import GameContext
from helpers import get_room_by_name
from rooms import world


@pytest.fixture(scope='function')
def game_context():
    context = GameContext(
        commands=[
            About(),
            Commands(),
            Down(),
            Drop(),
            East(),
            Examine(),
            Help(),
            Inventory(),
            LookAround(),
            North(),
            Quit(),
            South(),
            Take(),
            Up(),
            Use(),
            West()
        ],
        rooms=world.rooms
    )

    context.current_room = get_room_by_name('v lietadle', context.rooms)

    yield context
