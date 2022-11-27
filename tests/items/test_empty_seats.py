import pytest

from helpers import parse_line, get_item_by_name
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

    @pytest.mark.parametrize("feature", [EXAMINABLE])
    def test_when_created_then_expect_features_movable_and_usable(self, item, feature):
        assert feature in item.features, f'Feature {feature} should be in item.'

    def test_when_examined_then_parachute_should_appear_in_plane(self, item, game_context):
        # act
        command = parse_line(f'preskumaj {item.name}', game_context)
        command.exec(game_context)

        item = get_item_by_name('padak', game_context.current_room.items)

        # assert
        assert item is not None, 'Parachute is not in room.'

    def test_when_examined_then_it_is_not_examinable_anymore(self, item, game_context):
        # act
        command = parse_line(f'preskumaj {item.name}', game_context)
        command.exec(game_context)

        item = get_item_by_name(item.name, game_context.current_room.items)

        # assert
        assert EXAMINABLE not in item.features, 'Empty seats are still examinable.'
