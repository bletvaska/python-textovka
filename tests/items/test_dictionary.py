import pytest

from adventure.items.dictionary import Dictionary
from adventure.items.features import MOVABLE, USABLE


@pytest.mark.items
@pytest.mark.dictionary
class TestSuiteDictionary:

    @pytest.fixture
    def item(self):
        yield Dictionary()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'slovnik'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Je to anglicko-staroegyptský slovník, 14. upravené vydanie.'

    def test_when_created_then_expect_features_movable_and_usable(self, item):
        # arrange
        expected = [MOVABLE, USABLE]

        # assert
        assert set(item.features) == set(expected), f'Item should have following features: {expected}.'
