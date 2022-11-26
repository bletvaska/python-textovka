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
