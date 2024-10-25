import pytest

from adventure.commands import About
from adventure.commands import Commands
from adventure.commands import Down
from adventure.commands import Drop
from adventure.commands import East
from adventure.commands import Examine
from adventure.commands import Help
from adventure.commands import Inventory
from adventure.commands import LookAround
from adventure.commands import North
from adventure.commands import Quit
from adventure.commands import South
from adventure.commands import Take
from adventure.commands import Up
from adventure.commands import Use
from adventure.commands import West

from adventure.game_context import GameContext
from adventure.helpers import get_room_by_name
from rooms.world import load_world


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
        rooms=load_world()
    )

    context.current_room = get_room_by_name('v lietadle', context)

    yield context
