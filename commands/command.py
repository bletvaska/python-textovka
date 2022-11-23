from dataclasses import dataclass

from game_context import GameContext


@dataclass
class Command:
    """
    Describes every command in game.
    """
    # fields
    name: str
    description: str

    # behavior / methods
    def exec(self, context: GameContext):
        #! FIXME exception
        print('vykonavam prikaz')
