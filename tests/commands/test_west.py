import pytest

from commands import West
from helpers import get_room_by_name, parse_line

pytestmark = [pytest.mark.commands, pytest.mark.west]


@pytest.fixture
def cmd():
    yield West()


def test_when_created_then_expect_specific_name(cmd):
    assert cmd.name == 'zapad'


def test_when_created_then_expect_specific_description(cmd):
    assert cmd.description == 'presunie sa do miestnosti na západ od aktuálnej'


def test_when_moves_to_west_then_new_room_must_be_on_west_from_actual(cmd, game_context):
    # arrange
    game_context.current_room = get_room_by_name('v tábore', game_context)

    # act
    command = parse_line(cmd.name, game_context)
    command.exec(game_context)

    # assert
    assert game_context.current_room.name == 'malý stan'


def test_if_there_is_no_room_on_west_then_current_room_remains_after_going_west(cmd, game_context):
    # act
    command = parse_line(cmd.name, game_context)
    command.exec(game_context)

    # assert
    assert game_context.current_room.name == 'v lietadle'


def test_if_there_is_no_room_on_west_then_error_message_should_appear(cmd, game_context, capsys):
    # act
    command = parse_line(cmd.name, game_context)
    command.exec(game_context)
    captured = capsys.readouterr()

    # assert
    assert captured.out == 'Tam sa nedá ísť.\n'
