import pytest

from commands.quit import Quit


@pytest.fixture
def cmd():
    return Quit()


def test_when_created_then_expect_specific_name(cmd):
    assert cmd.name == 'koniec'


def test_when_created_then_expect_specific_description(cmd):
    assert cmd.description == 'ukončí hru'


def test_when_no_is_entered_then_game_state_remains_playing(cmd):
    pass
