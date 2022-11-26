import pytest

from commands.commands import Commands


@pytest.mark.commands
class TestSuiteCommands:

    @pytest.fixture(scope='class')
    def cmd(self):
        return Commands()

    def test_when_created_then_expect_specific_name(self, cmd):
        assert cmd.name == 'prikazy'

    def test_when_created_then_expect_specific_description(self, cmd):
        assert cmd.description == 'zobrazí dostupné príkazy v hre'
