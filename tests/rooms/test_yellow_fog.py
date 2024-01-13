import pytest

from adventure.helpers import parse_line
from adventure.rooms import directions
from adventure.rooms.yellow_fog import YellowFog

pytestmark = [pytest.mark.rooms, pytest.mark.yellow_fog]


@pytest.fixture
def room():
    yield YellowFog(
        name='žltá hmla',
        description='Si v žltej hmle.',
        exits={
            directions.EAST: 'chodba',
            directions.WEST: 'žltá hmla',
            directions.SOUTH: 'žltá hmla',
            directions.NORTH: 'žltá hmla',
        })


@pytest.mark.parametrize('direction', ['sever', 'juh', 'zapad'])
def test_when_first_step_is_made_then_all_exits_goes_to_yellow_fog_and_east_goes_to_chodba(room, game_context,
                                                                                           direction):
    # arrange
    game_context.current_room = room

    # act
    command = parse_line(direction, game_context)
    command.exec(game_context)
    game_context.current_room.act(game_context)

    # assert
    assert room.exits == {
        directions.NORTH: room.name,
        directions.SOUTH: room.name,
        directions.WEST: room.name,
        directions.EAST: 'chodba'
    }
