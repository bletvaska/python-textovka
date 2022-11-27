import pytest

from items.features import USABLE, MOVABLE
from items.parachute import Parachute


@pytest.mark.items
@pytest.mark.parachute
class TestSuiteParachute:

    @pytest.fixture(scope='class')
    def item(self):
        yield Parachute()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'padak'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Obyčajný padák. Made in U.S.A. 1933'

    @pytest.mark.parametrize("feature", [MOVABLE, USABLE])
    def test_when_created_then_expect_features_movable_and_usable(self, item, feature):
        assert feature in item.features, f'Feature {feature} should be in item.'
