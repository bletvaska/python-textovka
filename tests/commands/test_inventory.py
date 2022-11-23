import pytest

from commands import Inventory


@pytest.fixture
def cmd():
    return Inventory()


def test_when_created_then_expect_specific_name(cmd):
    assert cmd.name == 'inventar'


def test_when_created_then_expect_specific_description(cmd):
    assert cmd.description == 'zobrazí obsah hráčovho batohu'
