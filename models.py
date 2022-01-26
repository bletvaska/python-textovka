from dataclasses import dataclass
import states


@dataclass
class Context:
    room: dict
    world: dict
    backpack: list
    commands: list
    state: str = states.PLAYING
