import pytest

from adventure.commands.look_around import LookAround

pytestmark = [pytest.mark.commands, pytest.mark.look_around]


@pytest.fixture
def cmd():
    yield LookAround()


def test_when_created_then_expect_specific_name(cmd):
    assert cmd.name == 'rozhliadni sa'


def test_when_created_then_expect_specific_description(cmd):
    assert cmd.description == 'rozhliadne sa v aktuálnej miestnosti'
