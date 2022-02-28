from dataclasses import dataclass

import states


@dataclass
class Context:
    world: dict
    room: dict
    backpack: list
    commands: list
    history: list
    game_state: str = states.PLAYING
