import pytest

import states
from helpers import parse_line

pytestmark = [pytest.mark.scenarios, pytest.mark.plane_crash]


@pytest.fixture
def scenario():
    yield (
        'preskumaj prazdne sedadla',
        'vezmi padak',
        'vezmi bic',
        'rozhliadni sa',
        'rozhliadni sa',
    )


def test_when_plane_crash_scenario_is_entered_then_game_state_should_plane_crash(scenario, game_context):
    for line in scenario:
        command = parse_line(line, game_context)
        command.exec(game_context)
        game_context.current_room.act(game_context)

    assert game_context.game_state == states.PLANE_CRASH
