import pytest

from adventure.items.diamond import Diamond
from adventure.items.features import MOVABLE


@pytest.mark.items
@pytest.mark.diamond
class TestSuiteDiamond:

    @pytest.fixture
    def item(self):
        yield Diamond()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'diamant', 'Incorrect name.'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Ťažký, neforemný drahý kameň.', 'Incorrect description.'

    def test_when_created_then_expect_features_movable_and_usable(self, item):
        # arrange
        expected = [MOVABLE]

        # assert
        assert set(item.features) == set(expected), f'Item should have following features: {expected}.'

