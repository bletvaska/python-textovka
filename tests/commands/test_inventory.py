import pytest

from commands.inventory import Inventory
from game_context import GameContext
from items.whip import Whip


@pytest.fixture
def cmd():
    return Inventory()


def test_when_created_then_expect_specific_name(cmd):
    assert cmd.name == 'inventar'


def test_when_created_then_expect_specific_description(cmd):
    assert cmd.description == 'zobrazí obsah hráčovho batohu'


def test_when_backpack_is_empty_then_expect_specific_message_on_stdout(cmd, capsys, game_context):
    game_context.backpack = []
    cmd.exec(game_context)
    captured = capsys.readouterr()

    assert captured.out == 'Batoh je prázdny.\n'


def test_when_backpack_has_items_then_print_its_content_on_stdout(cmd, capsys, game_context):
    game_context.backpack = [Whip()]
    cmd.exec(game_context)
    captured = capsys.readouterr()

    assert captured.out == ('V batohu máš:\n'
                            '* bic\n')
