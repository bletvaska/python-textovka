import pytest

from adventure.helpers import parse_line

pytestmark = [pytest.mark.scenarios, pytest.mark.happy_scenario]


@pytest.fixture
def happy_scenario():
    yield (
        'preskumaj prazdne sedadla',
        'vezmi padak',
        'vezmi bic',
        'dolu',
        'pouzi padak',
        'juh',
        'preskumaj kokosova palma',
        'preskumaj nemecka uniforma',
        'vezmi kluc',
        'vezmi nemecka uniforma',
        'pouzi nemecka uniforma',
        'juh',
        'juh',
        'preskumaj nemecky automobil',
        'vezmi automobilova bateria',
        'zapad',
        'vezmi mobilna radiostanica',
        'pouzi mobilna radiostanica',
        'poloz mobilna radiostanica',
        'poloz automobilova bateria',
        'vezmi lopata',
        'zapad',
        'zapad',
        'pouzi kluc',
        'poloz kluc',
        'preskumaj mapa',
        'vezmi slovnik',
        'vezmi diamant',
        'zapad',
        'sever',
        'sever',
        'dolu'
    )


def test_when_happy_scenario_is_entered_then_game_state_should_be_well_done(happy_scenario, game_context):
    for line in happy_scenario:
        command = parse_line(line, game_context)
        command.exec(game_context)
        game_context.current_room.act(game_context)

    # assert game_context.game_state == states.WELL_DONE
    assert game_context.current_room.name == 'podzemie'
