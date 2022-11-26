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
    param: str = None

    # behavior / methods
    def exec(self, context: GameContext) -> None:
        raise NotImplemented(f'Príkaz {self.name} ešte nebol implementovaný.')
