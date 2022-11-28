import pytest

from helpers import get_room_by_name, get_item_by_name
from items.features import MOVABLE, USABLE
from items.whip import Whip


@pytest.mark.items
@pytest.mark.whip
class TestSuiteWhip:

    @pytest.fixture
    def item(self):
        yield Whip()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'bic', 'Incorrect name.'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Tvoj neoceniteľný pomocník..!', 'Incorrect description.'

    def test_when_created_then_expect_features_movable_and_usable(self, item):
        # arrange
        expected = [MOVABLE, USABLE]

        # assert
        assert set(item.features) == set(expected), f'Item should have following features: {expected}.'

    def test_when_used_then_success_message_should_appear(self, game_context, item, capsys):
        # arrange
        game_context.current_room = get_room_by_name('komôrka', game_context)

        # act
        item.use(game_context)
        captured = capsys.readouterr()

        # assert
        assert captured.out == 'Podarilo sa ti zraziť diamant dolu!\n', 'Invalid message appeared.'

    def test_when_used_then_true_should_be_returned(self, game_context, item):
        # arrange
        game_context.current_room = get_room_by_name('komôrka', game_context)

        # assert
        assert item.use(game_context) is True, 'True should be returned.'

    def test_when_used_successfully_then_diamond_should_appear_in_room(self, game_context, item):
        # arrange
        game_context.current_room = get_room_by_name('komôrka', game_context)

        # act
        item.use(game_context)
        diamond = get_item_by_name('diamant', game_context.current_room.items)

        # assert
        assert diamond.name is not None, 'Diamond should appear in the room.'

    def test_when_used_successfully_then_diamond_on_ceiling_should_dissapear(self, game_context, item):
        # arrange
        game_context.current_room = get_room_by_name('komôrka', game_context)

        # act
        item.use(game_context)
        diamond = get_item_by_name('diamant pri strope', game_context.current_room.items)

        # assert
        assert diamond is None, 'Diamond near ceiling should disappear.'
