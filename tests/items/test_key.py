import pytest

from items.features import USABLE, MOVABLE
from items.key import Key
from items.nazi_uniform import NaziUniform


@pytest.mark.items
@pytest.mark.key
class TestSuiteKey:

    @pytest.fixture(scope='class')
    def item(self):
        yield Key()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'kluc'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Veľký mosadzný kľúč, zrejme od nejakej truhly.'

    def test_when_created_then_expect_features_movable_and_usable(self, item):
        # arrange
        expected = [MOVABLE, USABLE]

        # assert
        assert set(item.features) == set(expected), f'Item should have following features: {expected}.'
