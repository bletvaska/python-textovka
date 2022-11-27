import pytest

from helpers import parse_line, get_room_by_name, get_item_by_name
from items.features import EXAMINABLE
from items.german_car import GermanCar


@pytest.mark.items
@pytest.mark.german_car
class TestSuiteGermanCar:

    @pytest.fixture(scope='class')
    def item(self):
        yield GermanCar()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'nemecky automobil', 'Incorrect name.'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Mercedes Benz, ale bohužiaľ v nepojazdnom stave.', 'Incorrect description.'

    def test_when_created_then_expect_features_movable_and_usable(self, item):
        # arrange
        expected = [EXAMINABLE]

        # assert
        assert set(item.features) == set(expected), f'Item should have following features: {expected}.'

    def test_when_examined_then_car_battery_should_appear_in_room(self, item, game_context):
        # arrange
        game_context.current_room = get_room_by_name('v tábore', game_context)

        # act
        command = parse_line(f'preskumaj {item.name}', game_context)
        command.exec(game_context)

        item = get_item_by_name('automobilova bateria', game_context.current_room.items)

        # assert
        assert item is not None, 'Car battery is not in room.'

    def test_when_examined_then_it_is_not_examinable_anymore(self, item, game_context):
        # arrange
        game_context.current_room = get_room_by_name('v tábore', game_context)

        # act
        command = parse_line(f'preskumaj {item.name}', game_context)
        command.exec(game_context)

        item = get_item_by_name(item.name, game_context.current_room.items)

        # assert
        assert EXAMINABLE not in item.features, 'German car is still examinable.'
