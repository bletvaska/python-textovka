import pytest

from commands import About
from commands import Commands
from commands import Down
from commands import Drop
from commands import East
from commands import Examine
from commands import Help
from commands import Inventory
from commands import LookAround
from commands import North
from commands import Quit
from commands import South
from commands import Take
from commands import Up
from commands import Use
from commands import West

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
