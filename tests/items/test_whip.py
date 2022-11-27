import pytest

from items.features import MOVABLE
from items.whip import Whip


@pytest.mark.items
@pytest.mark.whip
class TestSuiteWhip:

    @pytest.fixture
    def item(self):
        yield Whip()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'bic'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Tvoj neoceniteľný pomocník..!'

    def test_when_created_then_expect_features_movable_and_usable(self, item):
        # arrange
        expected = [MOVABLE]

        # assert
        assert set(item.features) == set(expected), f'Item should have following features: {expected}.'
