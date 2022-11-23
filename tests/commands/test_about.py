import pytest

from commands.about import About


@pytest.fixture
def cmd():
    return About()


def test_when_created_then_expect_specific_name(cmd):
    assert cmd.name == 'o hre'


def test_when_created_then_expect_specific_description(cmd):
    assert cmd.description == 'zobrazí informácie o hre'
