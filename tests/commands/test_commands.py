import pytest

from commands import Commands

pytestmark = [pytest.mark.commands, pytest.mark.commands]


@pytest.fixture(scope='module')
def cmd():
    return Commands()


def test_when_created_then_expect_specific_name(cmd):
    assert cmd.name == 'prikazy'


def test_when_created_then_expect_specific_description(cmd):
    assert cmd.description == 'zobrazí dostupné príkazy v hre'
