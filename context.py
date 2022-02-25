from dataclasses import dataclass

import states


@dataclass
class Context:
    room: dict
    backpack: list
    game_state: str = states.PLAYING
