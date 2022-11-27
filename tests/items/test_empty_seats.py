import pytest

from items.empty_seats import EmptySeats
from items.features import EXAMINABLE


@pytest.mark.items
@pytest.mark.empty_seats
class TestSuiteParachute:

    @pytest.fixture(scope='class')
    def item(self):
        yield EmptySeats()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'prazdne sedadla'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Obyčajné letecké sedadlá.'

    @pytest.mark.wip
    @pytest.mark.parametrize("feature", [EXAMINABLE])
    def test_when_created_then_expect_features_movable_and_usable(self, item, feature):
        assert feature in item.features, f'Feature {feature} should be in item.'
