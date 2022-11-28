import pytest

from items.diamond_on_ceiling import DiamondOnCeiling
from items.features import MOVABLE


@pytest.mark.items
@pytest.mark.diamond_on_ceiling
class TestSuiteDiamondOnCeiling:

    @pytest.fixture
    def item(self):
        yield DiamondOnCeiling()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'diamant pri strope', 'Incorrect name.'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Leží na malom výstupku tesne pri strope miestnosti, asi dva metre nad tvojou ' \
                                   'hlavou.', 'Incorrect description. '

    def test_when_created_then_expect_no_features(self, item):
        assert item.features == [], f'Item features should be empty.'

