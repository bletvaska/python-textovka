import pytest

from adventure.items.car_battery import CarBattery
from adventure.items.features import MOVABLE, USABLE
from adventure.items.mobile_radiostation import MobileRadiostation


@pytest.mark.items
@pytest.mark.whip
class TestSuiteMobileRadiostation:

    @pytest.fixture
    def item(self):
        yield MobileRadiostation()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'prenosnu radiostanicu', 'Incorrect name.'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Zdá sa, že je schopná prevádzky.', 'Incorrect description.'

    def test_when_created_then_expect_features_movable_and_usable(self, item):
        # arrange
        expected = [MOVABLE, USABLE]

        # assert
        assert set(item.features) == set(expected), f'Item should have following features: {expected}.'

    def test_when_used_without_battery_then_specific_message_should_appear(self, game_context, item, capsys):
        # arrange
        game_context.backpack.append(item)

        # act
        item.on_use(game_context)
        captured = capsys.readouterr()

        # assert
        assert captured.out == 'Bohužiaľ, nemáš žiadny zdroj elektriny.\n', 'Incorrect message.'

    # @pytest.skip
    # def test_when_used_with_battery_then_specific_message_should_appear(self, game_context, item, capsys):
    #     # arrange
    #     game_context.backpack.append(item)
    #     game_context.backpack.append(CarBattery())
    #
    #     # act
    #     item.on_use(game_context)
    #     captured = capsys.readouterr()
    #
    #     # assert
    #     assert captured.out == 'Podarilo sa ti spojiť s priateľmi v Káhire. Sľúbili, že po teba pošlú lietadlo.\n' \
    #                            'Ale niečo za niečo... Chcú, aby si našiel faraónov platinový náhrdelník, ' \
    #                            'ktorý Nemci hľadajú už niekoľko mesiacov.\n', 'Incorrect message.'
