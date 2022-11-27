import pytest

from items.features import USABLE, MOVABLE
from items.showel import Showel


@pytest.mark.items
@pytest.mark.showel
class TestSuiteShowel:

    @pytest.fixture
    def item(self):
        yield Showel()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'lopata'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Je to zázrak, že ešte drží pohromade...'

    def test_when_created_then_expect_features_movable_and_usable(self, item):
        # arrange
        expected = [MOVABLE, USABLE]

        # assert
        assert set(item.features) == set(expected), f'Item should have following features: {expected}.'
