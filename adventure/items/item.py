from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from game_context import GameContext


class Item(BaseModel):
    name: str
    description: str
    features: list[int] = []

    def use(self, context: 'GameContext'):
        raise NotImplementedError('Usage of item was not yet implemented.')

    def examine(self, context: 'GameContext'):
        raise NotImplementedError('Examination of item was not yet implemented.')
