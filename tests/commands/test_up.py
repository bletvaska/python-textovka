import pytest

from commands.up import Up
from helpers import parse_line


@pytest.fixture
def cmd():
    yield Up()


def test_when_created_then_expect_specific_name(cmd):
    assert cmd.name == 'hore'


def test_when_created_then_expect_specific_description(cmd):
    assert cmd.description == 'presunie sa do miestnosti hore od aktuálnej'


def test_if_there_is_no_room_up_then_current_room_remains_after_going_up(cmd, game_context):
    # act
    command = parse_line(cmd.name, game_context.commands)
    command.exec(game_context)

    # assert
    assert game_context.current_room.name == 'v lietadle'


def test_if_there_is_no_room_up_then_error_message_should_appear(cmd, game_context, capsys):
    # act
    command = parse_line(cmd.name, game_context.commands)
    command.exec(game_context)
    captured = capsys.readouterr()

    # assert
    assert captured.out == 'Tam sa nedá ísť.\n'
