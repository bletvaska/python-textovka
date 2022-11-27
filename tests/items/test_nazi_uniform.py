import pytest

from helpers import parse_line, get_item_by_name, get_room_by_name
from items.features import USABLE, MOVABLE, EXAMINABLE
from items.nazi_uniform import NaziUniform


@pytest.mark.items
@pytest.mark.nazi_uniform
class TestSuiteNaziUniform:

    @pytest.fixture
    def item(self):
        yield NaziUniform()

    def test_when_created_then_expect_specific_name(self, item):
        assert item.name == 'nemecka uniforma', 'Incorrect name.'

    def test_when_created_then_expect_specific_description(self, item):
        assert item.description == 'Zachovalá dôstojnícka uniforma.', 'Incorrect description.'

    def test_when_created_then_expect_features_movable_and_usable(self, item):
        # arrange
        expected = [MOVABLE, USABLE, EXAMINABLE]

        # assert
        assert set(item.features) == set(expected), f'Item should have following features: {expected}.'

    def test_when_examined_then_key_should_appear_room(self, item, game_context):
        # arrange
        game_context.current_room = get_room_by_name('oáza', game_context)
        command = parse_line(f'preskumaj kokosova palma', game_context)
        command.exec(game_context)

        # act
        command = parse_line(f'preskumaj {item.name}', game_context)
        command.exec(game_context)

        item = get_item_by_name('kluc', game_context.current_room.items)

        # assert
        assert item is not None, 'Key is not in room.'

    def test_when_examined_then_it_is_not_examinable_anymore(self, item, game_context):
        # arrange
        game_context.current_room = get_room_by_name('oáza', game_context)
        command = parse_line(f'preskumaj kokosova palma', game_context)
        command.exec(game_context)

        # act
        command = parse_line(f'preskumaj {item.name}', game_context)
        command.exec(game_context)

        item = get_item_by_name('kluc', game_context.current_room.items)

        # assert
        assert EXAMINABLE not in item.features, 'Empty seats are still examinable.'
