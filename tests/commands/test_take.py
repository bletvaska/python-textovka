import pytest

from commands.take import Take

pytestmark = [pytest.mark.commands, pytest.mark.take]


@pytest.fixture
def cmd():
    yield Take()


def test_when_created_then_expect_specific_name(cmd):
    assert cmd.name == 'vezmi'


def test_when_created_then_expect_specific_description(cmd):
    assert cmd.description == 'vezme predmet z miestnosti a vloží ho do batohu'
