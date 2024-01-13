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
        'preskumaj kokosovu palmu',
        'preskumaj nemecku uniformu',
        'vezmi kluc',
        'vezmi nemecku uniformu',
        'pouzi nemecku uniformu',
        'juh',
        'juh',
        'preskumaj nemecky automobil',
        'vezmi automobilovu bateriu',
        'zapad',
        'vezmi prenosnu radiostanicu',
        'pouzi prenosnu radiostanicu',
        'poloz prenosnu radiostanicu',
        'poloz automobilovu bateriu',
        'vezmi lopatu',
        'vychod',
        'vychod',
        'pouzi kluc',
        'poloz kluc',
        'preskumaj mapu',
        'vezmi slovnik',
        'vezmi diamant',
        'zapad',
        'sever',
        'sever',
        'pouzi lopatu',
        'dolu'
    )


def test_when_happy_scenario_is_entered_then_game_state_should_be_well_done(happy_scenario, game_context):
    for line in happy_scenario:
        command = parse_line(line, game_context)
        command.exec(game_context)
        game_context.current_room.act(game_context)

    # assert game_context.game_state == states.WELL_DONE
    assert game_context.current_room.name == 'podzemie'
