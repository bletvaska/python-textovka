import pytest

from commands.help import Help


@pytest.fixture
def cmd():
    return Help()


def test_when_created_then_expect_specific_name(cmd):
    assert cmd.name == 'pomoc'


def test_when_created_then_expect_specific_description(cmd):
    assert cmd.description == 'zobrazí pomocníka ku zvolenému príkazu'
