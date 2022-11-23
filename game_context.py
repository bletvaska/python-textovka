from dataclasses import dataclass, field

from states import STATE_PLAYING


@dataclass
class GameContext:
    backpack: list[str] = field(default_factory=list)
    commands: list = field(default_factory=list)
    game_state: str = STATE_PLAYING
