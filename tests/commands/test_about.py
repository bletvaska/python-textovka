import pytest

from commands.about import About


@pytest.mark.commands
@pytest.mark.about
class TestSuiteAbout:

    @pytest.fixture(scope='class')
    def cmd(self):
        yield About()

    def test_when_created_then_expect_specific_name(self, cmd):
        assert cmd.name == 'o hre'

    def test_when_created_then_expect_specific_description(self, cmd):
        assert cmd.description == 'zobrazí informácie o hre'
