import pytest

from commands.about import About
from commands.command import Command
from commands.commands import Commands
from commands.help import Help
from commands.inventory import Inventory
from commands.quit import Quit
from helpers import parse_line


def test_when_empty_line_is_given_then_expect_none(game_context):
    assert parse_line('', game_context.commands) is None


def test_when_unknown_string_is_given_then_expect_none(faker, game_context):
    assert parse_line(faker.sentence(), game_context.commands) is None


@pytest.mark.parametrize("command", [About(), Commands(), Help(), Inventory(), Quit()])
def test_when_valid_command_is_given_then_expect_result_of_type_command(command, game_context):
    result = parse_line(command.name, game_context.commands)
    assert isinstance(result, Command) is True, 'Returning object is not of type Command'
