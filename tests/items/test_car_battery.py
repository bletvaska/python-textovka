import pytest

from adventure.items.car_battery import CarBattery
from adventure.items.features import MOVABLE


@pytest.mark.items
@pytest.mark.car_battery
class TestSuiteCarBattery:

    @pytest.fixture
    def item(self):
        yield CarBattery()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'automobilovu bateriu', 'Incorrect name.'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Ešte je trochu nabitá.', 'Incorrect description.'

    def test_when_created_then_expect_features_movable_and_usable(self, item):
        # arrange
        expected = [MOVABLE]

        # assert
        assert set(item.features) == set(expected), f'Item should have following features: {expected}.'
