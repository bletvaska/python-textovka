from pydantic import BaseModel

from game_context import GameContext


class Command(BaseModel):
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
