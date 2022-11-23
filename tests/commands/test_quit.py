import io
import sys

import pytest

from commands.quit import Quit
from game_context import GameContext
from states import STATE_PLAYING, STATE_QUIT


@pytest.fixture
def cmd():
    return Quit()


def test_when_created_then_expect_specific_name(cmd):
    assert cmd.name == 'koniec'


def test_when_created_then_expect_specific_description(cmd):
    assert cmd.description == 'ukončí hru'


@pytest.mark.parametrize("choice", ['no', 'n', 'nie', 'lorem ipsum', ''])
def test_when_no_is_entered_then_game_state_remains_playing(cmd, choice):
    sys.stdin = io.StringIO(f'{choice}\n')
    context = GameContext()
    cmd.exec(context, None)

    assert context.game_state == STATE_PLAYING


@pytest.mark.parametrize("choice", ['ano', 'a', 'yes', 'y'])
def test_when_yes_is_entered_then_game_state_changes_to_quit(cmd, choice):
    sys.stdin = io.StringIO(f'{choice}\n')
    context = GameContext()
    cmd.exec(context, None)

    assert context.game_state == STATE_QUIT
