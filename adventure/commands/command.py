from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_context import GameContext

from pydantic import BaseModel


class Command(BaseModel):
    name: str
    description: str

    def exec(self, context: "GameContext", param: str):
        raise NotImplementedError('This method is not implemented.')
