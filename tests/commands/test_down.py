import pytest

from adventure.commands.down import Down
from adventure.helpers import get_room_by_name, parse_line
from adventure.game_context import GameContext

pytestmark = [pytest.mark.commands, pytest.mark.down]


@pytest.fixture(scope='module')
def game_context():
    yield GameContext(
        commands=[
            Down()
        ]
    )


@pytest.fixture(scope='module')
def cmd():
    yield Down()


def test_when_created_then_expect_specific_name(cmd):
    assert cmd.name == 'dolu'


def test_when_created_then_expect_specific_description(cmd):
    assert cmd.description == 'presunie sa do miestnosti dolu od aktuálnej'


def test_when_moves_down_then_new_room_must_be_down_from_actual(cmd, game_context):
    # arrange
    game_context.current_room = get_room_by_name('v lietadle', game_context)

    # act
    command = parse_line(cmd.name, game_context)
    command.exec(game_context)

    # assert
    assert game_context.current_room.name == 'voľný pád'


def test_if_there_is_no_room_down_then_current_room_remains_after_going_down(cmd, game_context):
    # arrange
    game_context.current_room = get_room_by_name('v tábore', game_context)

    # act
    command = parse_line(cmd.name, game_context)
    command.exec(game_context)

    # assert
    assert game_context.current_room.name == 'v tábore'


def test_if_there_is_no_room_down_then_error_message_should_appear(cmd, game_context, capsys):
    # arrange
    game_context.current_room = get_room_by_name('v tábore', game_context)

    # act
    command = parse_line(cmd.name, game_context)
    command.exec(game_context)
    captured = capsys.readouterr()

    # assert
    assert captured.out == 'Tam sa nedá ísť.\n'
