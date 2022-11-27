import pytest

from helpers import parse_line, get_room_by_name, get_item_by_name
from items.coconut_palm_tree import CoconutPalmTree
from items.features import EXAMINABLE


@pytest.mark.items
@pytest.mark.coconut_palm_tree
class TestSuiteCoconutPalmTree:

    @pytest.fixture
    def item(self):
        yield CoconutPalmTree()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'kokosova palma'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Zdá sa, že na jej plody nedosiahneš.'

    def test_when_created_then_expect_features_movable_and_usable(self, item,):
        # arrange
        expected = [EXAMINABLE]

        # assert
        assert set(item.features) == set(expected), f'Item should have following features: {expected}.'

    def test_when_examined_then_nazi_uniform_should_appear_in_room(self, item, game_context):
        # arrange
        game_context.current_room = get_room_by_name('oáza', game_context)

        # act
        command = parse_line(f'preskumaj {item.name}', game_context)
        command.exec(game_context)

        item = get_item_by_name('nemecka uniforma', game_context.current_room.items)

        # assert
        assert item is not None, 'Nazi uniform is not in room.'

    def test_when_examined_then_it_is_not_examinable_anymore(self, item, game_context):
        # arrange
        game_context.current_room = get_room_by_name('oáza', game_context)

        # act
        command = parse_line(f'preskumaj {item.name}', game_context)
        command.exec(game_context)

        item = get_item_by_name(item.name, game_context.current_room.items)

        # assert
        assert EXAMINABLE not in item.features, 'Empty seats are still examinable.'
