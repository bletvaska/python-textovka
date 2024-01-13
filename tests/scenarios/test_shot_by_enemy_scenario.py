import pytest

from adventure import states
from adventure.helpers import parse_line

pytestmark = [pytest.mark.scenarios, pytest.mark.shot_by_enemy]


@pytest.fixture
def scenario():
    yield (
        'preskumaj prazdne sedadla',
        'vezmi padak',
        'vezmi bic',
        'dolu',
        'pouzi padak',
        'juh',
        'juh'
    )


def test_when_shot_by_enemy_scenario_is_entered_then_game_state_should_be_shot_by_enemy(scenario, game_context):
    for line in scenario:
        command = parse_line(line, game_context)
        command.exec(game_context)
        game_context.current_room.act(game_context)

    assert game_context.game_state == states.SHOT_BY_ENEMY
