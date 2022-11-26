import pytest

import states
from helpers import parse_line

pytestmark = [pytest.mark.scenarios, pytest.mark.free_fall]


@pytest.fixture
def scenario():
    yield (
        'preskumaj prazdne sedadla',
        'vezmi padak',
        'vezmi bic',
        'dolu',
        'dolu',
    )


def test_when_free_fall_scenario_is_entered_then_game_state_should_be_death_by_free_fall(scenario, game_context):
    # act
    for line in scenario:
        command = parse_line(line, game_context.commands)
        command.exec(game_context)
        game_context.current_room.act(game_context)

    # assert
    assert game_context.game_state == states.DEATH_BY_FREE_FALL
