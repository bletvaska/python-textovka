import pytest

from adventure.commands.about import About
from adventure.commands.commands import Commands
from adventure.commands.down import Down
from adventure.commands.drop import Drop
from adventure.commands.east import East
from adventure.commands.examine import Examine
from adventure.commands.help import Help
from adventure.commands.inventory import Inventory
from adventure.commands.look_around import LookAround
from adventure.commands.north import North
from adventure.commands.quit import Quit
from adventure.commands.south import South
from adventure.commands.take import Take
from adventure.commands.up import Up
from adventure.commands.use import Use
from adventure.commands.west import West

pytestmark = [pytest.mark.commands, pytest.mark.help]


@pytest.fixture
def cmd():
    return Help()


def test_when_created_then_expect_specific_name(cmd):
    assert cmd.name == 'pomoc'


def test_when_created_then_expect_specific_description(cmd):
    assert cmd.description == 'zobrazí pomocníka ku zvolenému príkazu'


def test_when_invoked_without_parameter_then_specific_message_should_appear(cmd, game_context, capsys):
    # act
    cmd.exec(game_context)
    captured = capsys.readouterr()

    # assert
    assert captured.out == 'Zatiaľ sa ti darí dosť dobre.\n'


@pytest.mark.parametrize("command", [About(),
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
                                     West()])
def test_when_invoked_without_the_name_of_command_then_command_description_should_appear(cmd, game_context, capsys,
                                                                                         command):
    # arrange
    cmd.param = command.name

    # act
    cmd.exec(game_context)
    captured = capsys.readouterr()

    # assert
    assert captured.out == f'{command.name} - {command.description}\n'
