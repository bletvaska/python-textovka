from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_context import GameContext

from pydantic import BaseModel


class Command(BaseModel):
    """
    Generic game command.
    """
    name: str
    description: str

    def exec(self, context: "GameContext"):
        raise NotImplementedError(f'This method was not yet implemented for command {self.name}.')
