import pytest

from commands.down import Down
from helpers import get_room_by_name, parse_line


@pytest.mark.commands
@pytest.mark.down
class TestSuiteDown:

    @pytest.fixture(scope='class')
    def cmd(self):
        yield Down()

    def test_when_created_then_expect_specific_name(self, cmd):
        assert cmd.name == 'dolu'

    def test_when_created_then_expect_specific_description(self, cmd):
        assert cmd.description == 'presunie sa do miestnosti dolu od aktuálnej'

    def test_when_moves_down_then_new_room_must_be_down_from_actual(self, cmd, game_context):
        # act
        command = parse_line(cmd.name, game_context.commands)
        command.exec(game_context)

        # assert
        assert game_context.current_room.name == 'voľný pád'

    def test_if_there_is_no_room_down_then_current_room_remains_after_going_down(self, cmd, game_context):
        # arrange
        game_context.current_room = get_room_by_name('v tábore', game_context.rooms)

        # act
        command = parse_line(cmd.name, game_context.commands)
        command.exec(game_context)

        # assert
        assert game_context.current_room.name == 'v tábore'

    def test_if_there_is_no_room_down_then_error_message_should_appear(self, cmd, game_context, capsys):
        # arrange
        game_context.current_room = get_room_by_name('v tábore', game_context.rooms)

        # act
        command = parse_line(cmd.name, game_context.commands)
        command.exec(game_context)
        captured = capsys.readouterr()

        # assert
        assert captured.out == 'Tam sa nedá ísť.\n'
