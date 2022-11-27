import pytest

from items.coconut_palm_tree import CoconutPalmTree
from items.features import EXAMINABLE


@pytest.mark.items
@pytest.mark.coconut_palm_tree
class TestSuiteCoconutPalmTree:

    @pytest.fixture(scope='class')
    def item(self):
        yield CoconutPalmTree()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'kokosova palma'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Zdá sa, že na jej plody nedosiahneš.'

    @pytest.mark.wip
    @pytest.mark.parametrize("feature", [EXAMINABLE])
    def test_when_created_then_expect_features_movable_and_usable(self, item, feature):
        assert feature in item.features, f'Feature {feature} should be in item.'
