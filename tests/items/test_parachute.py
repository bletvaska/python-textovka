import pytest

from adventure.helpers import get_room_by_name
from adventure.items.features import USABLE, MOVABLE
from adventure.items.parachute import Parachute


@pytest.mark.items
@pytest.mark.parachute
class TestSuiteParachute:

    @pytest.fixture
    def item(self):
        yield Parachute()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'padak', 'Incorrect name.'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Obyčajný padák. Made in U.S.A. 1933', 'Incorrect description.'

    def test_when_created_then_expect_features_movable_and_usable(self, item):
        # arrange
        expected = [MOVABLE, USABLE]

        # assert
        assert set(item.features) == set(expected), f'Item should have following features: {expected}.'

    def test_when_used_then_expect_specific_message(self, item, game_context, capsys):
        # arrange
        game_context.current_room = get_room_by_name('voľný pád', game_context)
        game_context.backpack.append(item)

        # act
        item.use(game_context)
        captured = capsys.readouterr()

        # assert
        assert captured.out.startswith('Nad hlavou sa ti roztvoril padák a po chvíli si šťastne pristál...\n'), \
            'Incorrect message.'

    def test_when_used_then_indy_should_apper_in_room_pust(self, game_context, item):
        # arrange
        game_context.current_room = get_room_by_name('voľný pád', game_context)
        game_context.backpack.append(item)

        # act
        item.use(game_context)

        # assert
        assert game_context.current_room.name == 'púšť', 'Indy should appear in room "púšť".'
