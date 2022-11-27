import pytest

from helpers import parse_line, get_room_by_name, get_item_by_name
from items.car_battery import CarBattery
from items.coconut_palm_tree import CoconutPalmTree
from items.features import EXAMINABLE, MOVABLE


@pytest.mark.items
@pytest.mark.car_battery
class TestSuiteCarBattery:

    @pytest.fixture(scope='class')
    def item(self):
        yield CarBattery()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'automobilova bateria', 'Incorrect name.'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Ešte je trochu nabitá.', 'Incorrect description.'

    def test_when_created_then_expect_features_movable_and_usable(self, item):
        # arrange
        expected = [MOVABLE]

        # assert
        assert set(item.features) == set(expected), f'Item should have following features: {expected}.'
