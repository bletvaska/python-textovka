from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_context import GameContext

from pydantic import BaseModel


class Command(BaseModel):
    """
    Describes every command in game.
    """
    # fields
    name: str
    description: str
    param: str = None

    # behavior / methods
    def exec(self, context: "GameContext") -> None:
        raise NotImplemented(f'Príkaz {self.name} ešte nebol implementovaný.')
