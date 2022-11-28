import pytest

from items.features import MOVABLE, USABLE
from items.whip import Whip


@pytest.mark.items
@pytest.mark.whip
class TestSuiteWhip:

    @pytest.fixture
    def item(self):
        yield Whip()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'bic', 'Incorrect name.'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Tvoj neoceniteľný pomocník..!', 'Incorrect description.'

    def test_when_created_then_expect_features_movable_and_usable(self, item):
        # arrange
        expected = [MOVABLE, USABLE]

        # assert
        assert set(item.features) == set(expected), f'Item should have following features: {expected}.'
