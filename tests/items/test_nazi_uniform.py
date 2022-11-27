import pytest

from items.features import USABLE, MOVABLE
from items.nazi_uniform import NaziUniform


@pytest.mark.items
@pytest.mark.nazi_uniform
class TestSuiteNaziUniform:

    @pytest.fixture(scope='class')
    def item(self):
        yield NaziUniform()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'nemecka uniforma'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Zachovalá dôstojnícka uniforma.'

    @pytest.mark.parametrize("feature", [MOVABLE, USABLE])
    def test_when_created_then_expect_features_movable_and_usable(self, item, feature):
        assert feature in item.features, f'Feature {feature} should be in item.'
