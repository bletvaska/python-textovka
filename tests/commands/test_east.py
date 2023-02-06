import pytest

from commands.east import East
from helpers import get_room_by_name, parse_line

pytestmark = [pytest.mark.commands, pytest.mark.east]


@pytest.fixture(scope='module')
def cmd():
    yield East()


def test_when_created_then_expect_specific_name(cmd):
    assert cmd.name == 'vychod'


def test_when_created_then_expect_specific_description(cmd):
    assert cmd.description == 'presunie sa do miestnosti na východ od aktuálnej'


def test_when_moves_to_east_then_new_room_must_be_on_east_from_actual(cmd, game_context):
    # arrange
    game_context.current_room = get_room_by_name('v tábore', game_context)

    # act
    command = parse_line(cmd.name, game_context)
    command.exec(game_context)

    # assert
    assert game_context.current_room.name == 'veliteľov stan'


def test_if_there_is_no_room_on_east_then_current_room_remains_after_going_east(cmd, game_context):
    # act
    command = parse_line(cmd.name, game_context)
    command.exec(game_context)

    # assert
    assert game_context.current_room.name == 'v lietadle'


def test_if_there_is_no_room_on_east_then_error_message_should_appear(cmd, game_context, capsys):
    # act
    command = parse_line(cmd.name, game_context)
    command.exec(game_context)
    captured = capsys.readouterr()

    # assert
    assert captured.out == 'Tam sa nedá ísť.\n'