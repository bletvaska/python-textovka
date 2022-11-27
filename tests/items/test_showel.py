import pytest

from helpers import get_room_by_name
from items.features import USABLE, MOVABLE
from items.showel import Showel
from rooms import directions


@pytest.mark.items
@pytest.mark.showel
class TestSuiteShowel:

    @pytest.fixture
    def item(self):
        yield Showel()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'lopata', 'Incorrect name.'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Je to zázrak, že ešte drží pohromade...', 'Incorrect description.'

    def test_when_created_then_expect_features_movable_and_usable(self, item):
        # arrange
        expected = [MOVABLE, USABLE]

        # assert
        assert set(item.features) == set(expected), f'Item should have following features: {expected}.'

    def test_when_used_then_expect_specific_message(self, item, game_context, capsys):
        # arrange
        game_context.current_room = get_room_by_name('oáza', game_context)
        game_context.backpack.append(item)

        # act
        item.use(game_context)
        captured = capsys.readouterr()

        # assert
        assert captured.out.startswith('Pod vrstvou piesku si objavil vchod do podzemia!\n'), 'Incorrect message.'

    def test_when_used_then_room_going_down_should_be_podzemie(self, game_context, item):
        # arrange
        game_context.current_room = get_room_by_name('oáza', game_context)
        game_context.backpack.append(item)

        # act
        item.use(game_context)

        # assert
        assert directions.DOWN in game_context.current_room.exits \
               and game_context.current_room.exits[directions.DOWN] == 'podzemie'
