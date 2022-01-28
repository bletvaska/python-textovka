from dataclasses import dataclass
import states


@dataclass
class Context:
    room: dict
    world: dict
    backpack: list[dict]
    commands: list
    history: list[str]
    state: str = states.PLAYING
