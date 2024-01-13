import pytest

from adventure.commands.south import South
from adventure.helpers import get_room_by_name, parse_line
from adventure.game_context import GameContext

pytestmark = [pytest.mark.commands, pytest.mark.south]


@pytest.fixture(scope='module')
def game_context():
    yield GameContext(
        commands=[
            South()
        ]
    )


@pytest.fixture
def cmd():
    yield South()


def test_when_created_then_expect_specific_name(cmd):
    assert cmd.name == 'juh'


def test_when_created_then_expect_specific_description(cmd):
    assert cmd.description == 'presunie sa do miestnosti na juh od aktuálnej'


def test_when_moves_to_south_then_new_room_must_be_on_south_from_actual(cmd, game_context):
    # arrange
    game_context.current_room = get_room_by_name('púšť', game_context)

    # act
    command = parse_line(cmd.name, game_context)
    command.exec(game_context)

    # assert
    assert game_context.current_room.name == 'oáza'


def test_if_there_is_no_room_on_south_then_current_room_remains_after_going_south(cmd, game_context):
    # arrange
    game_context.current_room = get_room_by_name('v lietadle', game_context)

    # act
    command = parse_line(cmd.name, game_context)
    command.exec(game_context)

    # assert
    assert game_context.current_room.name == 'v lietadle'


def test_if_there_is_no_room_on_south_then_error_message_should_appear(cmd, game_context, capsys):
    # arrange
    game_context.current_room = get_room_by_name('v lietadle', game_context)
    
    # act
    command = parse_line(cmd.name, game_context)
    command.exec(game_context)
    captured = capsys.readouterr()

    # assert
    assert captured.out == 'Tam sa nedá ísť.\n'
