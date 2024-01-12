import pytest

from adventure.commands.about import About

pytestmark = [pytest.mark.commands, pytest.mark.about]


@pytest.fixture(scope='module')
def cmd():
    yield About()


def test_when_created_then_expect_specific_name(cmd):
    assert cmd.name == 'o hre'


def test_when_created_then_expect_specific_description(cmd):
    assert cmd.description == 'zobrazí informácie o hre'
