import pytest

from commands.about import About


@pytest.mark.items
class TestAbout:

    @pytest.fixture
    def cmd(self):
        yield About()

    def test_when_created_then_expect_specific_name(self, cmd):
        assert cmd.name == 'o hre'

    def test_when_created_then_expect_specific_description(self, cmd):
        assert cmd.description == 'zobrazí informácie o hre'
