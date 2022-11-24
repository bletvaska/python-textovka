import pytest

from commands.look_around import LookAround


@pytest.fixture
def cmd():
    return LookAround()


def test_when_created_then_expect_specific_name(cmd):
    assert cmd.name == 'rozhliadni sa'


def test_when_created_then_expect_specific_description(cmd):
    assert cmd.description == 'rozhliadne sa v aktuálnej miestnosti'
