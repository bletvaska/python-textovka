import pytest

from commands.about import About
from commands.commands import Commands
from commands.help import Help
from commands.inventory import Inventory
from commands.look_around import LookAround
from commands.quit import Quit
from game_context import GameContext


@pytest.fixture
def game_context():
    yield GameContext(
        commands=[
            About(),
            Commands(),
            Help(),
            Inventory(),
            LookAround(),
            Quit()
        ],
        current_room='v lietadle'
    )
