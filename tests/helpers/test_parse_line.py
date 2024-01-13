import pytest

from adventure.commands.command import Command
from adventure.helpers import parse_line


def test_when_empty_line_is_given_then_expect_none(game_context):
    assert parse_line('', game_context) is None


def test_when_unknown_string_is_given_then_expect_none(faker, game_context):
    assert parse_line(faker.sentence(), game_context) is None


@pytest.mark.parametrize("line",
                         ['o hre', 'prikazy', 'pomoc', 'inventar', 'koniec', 'sever', 'juh', 'vychod', 'zapad', 'hore',
                          'dolu', 'vezmi', 'poloz', 'pouzi', 'preskumaj'])
def test_when_valid_command_is_given_then_expect_result_of_type_command(line, game_context):
    command = parse_line(line, game_context)
    assert isinstance(command, Command) is True, 'Returning object is not of type Command'
